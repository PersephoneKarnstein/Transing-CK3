#!/usr/bin/env python3
"""Keep the whole of CK3's error.log through a long observe run.

The game stops writing error.log after 100,000 errors (the count the console command Log.ClearErrorLog resets; both
observe runs 24 and 25 stopped at exactly 100,000, about 40 minutes in, mostly vanilla's support_candidacy errors).
This script reads everything the game writes as it goes, so nothing is lost when the log is cleared. It keeps only
the mod's errors (entries that name a tm_ file, key or scope; with --all, everything), counts the game's own errors by
the file they come from, and warns when the count nears the cap so that you can clear it from the console (the game must run with
-debug_mode, as the observe runs do):

    open the console, type   Log.ClearErrorLog   and press Return.

With --auto-clear it types that command into the game itself, through macOS System Events (console key ` by
default). It checks at start that the terminal app has the permissions this needs (Automation of System Events and
Accessibility) and refuses to start if not. Until the log is cleared it warns once a minute with a beep; auto-clear is
tried twice, then left to you.

Usage (start it after the game is running; it stops by itself when the game quits):
    python3 tools/errorlog_keeper.py [--auto-clear] [--console-key '`'] [--threshold 95000]

Output, outside the repo: <logs>/archive/ours_<date>_<time>.log (the mod's errors) and, at the end,
<logs>/archive/summary_<date>_<time>.txt: the mod's errors counted by where they were raised, the mod's known
harmless errors counted by kind (KNOWN below; not kept in the log), and the game's own errors counted by source
file. With --all, also <logs>/archive/error_<date>_<time>.log (everything).

The game's own errors that only touch the mod are counted with the game's, marked: "[inside our hook]" (a tm_
on_action or effect only in the call stack) or "[names our faith or a character of ours]" (our faith's name only in
the error's tooltip text, e.g. a vanilla conversion refused).
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
import time

LOGS = os.path.expanduser('~/Documents/Paradox Interactive/Crusader Kings III/logs')
CAP = 100_000
ENTRY = b'][E]['
HEAD = re.compile(rb'^\[\d\d:\d\d:\d\d\]\[')           # the first line of an entry
OURS = re.compile(rb'(?<![A-Za-z0-9_])tm_')                  # our files, keys, scopes and variables all start tm_
LOC = re.compile(rb'Script location: file: (\S+)')
CPP = re.compile(rb'\]\[(\w+\.cpp):')
STACK = re.compile(rb'^\s+file: ')                          # call-stack lines under "Script location"
MARKUP = re.compile(rb'(?:TOOLTIP|ONCLICK):\w+,[^ !]*')       # loc markup: a vanilla error that only shows our faith's name
# The mod's errors known to be harmless, counted in the summary instead of kept.
KNOWN = [
    (re.compile(rb"left was 'faith', right was 'rite'"),
     'tenet is_shown checked on a rite (1.20 asks it of both; tm_tenet_types.txt)'),
    (re.compile(rb"Variable 'tm_\w+' is set but is never used"),
     "variable set but never read by script (census counters, read from the save by census_report.py)"),
    (re.compile(rb"Variable 'tm_\w+' is used but is never set"),
     'variable used but never set (made by change_variable or kept from old saves)'),
]


def game_running():
    return subprocess.run(['pgrep', '-f', 'ck3 '], capture_output=True).returncode == 0


def osascript(script):
    r = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return r.returncode == 0, (r.stderr or r.stdout).strip()


def check_auto_clear_access():
    """Ask System Events about the game's windows: the same two permissions the keystrokes need (Automation of
    System Events, and Accessibility), without typing anything. The first run also brings up macOS's prompts."""
    ok, msg = osascript('tell application "System Events" to tell (first process whose name is "ck3") '
                        'to get count of windows')
    if ok:
        return None
    if '-1743' in msg:
        return ('this terminal app may not control System Events. In System Settings > Privacy & Security > '
                'Automation, allow it to control "System Events", then start the script again.')
    if '-1719' in msg or '-25211' in msg or 'assistive' in msg.lower():
        return ('this terminal app has no Accessibility permission. In System Settings > Privacy & Security > '
                'Accessibility, turn it on for the app you run the script from (Terminal, iTerm, VS Code...), '
                'then start the script again.')
    return f'System Events refused the test ({msg}).'


def auto_clear(console_key):
    ok, msg = osascript(f'''
tell application "System Events"
    set frontmost of (first process whose name is "ck3") to true
    delay 0.5
    keystroke "{console_key}"
    delay 0.5
    keystroke "Log.ClearErrorLog"
    key code 36
    delay 0.5
    keystroke "{console_key}"
end tell
''')
    if not ok:
        print(f'  auto-clear failed: {msg}', flush=True)
    return ok


def classify(text):
    """('ours', location), ('known', label) or ('vanilla', source file) for one log entry."""
    lines = text.splitlines(keepends=True)
    own = b''.join(l for l in lines if not STACK.match(l))     # the entry without its call stack
    m = LOC.search(text) or CPP.search(text)
    where = m.group(1).decode(errors='replace') if m else '(unknown)'
    if OURS.search(MARKUP.sub(b'', own)):
        for pat, label in KNOWN:
            if pat.search(own):
                return 'known', label
        m = re.search(rb'Script location: file: (\S+) line: \d+ \(([^)]*)\)', text)
        return 'ours', (f'{m.group(1).decode()} ({m.group(2).decode()})' if m else where)
    if OURS.search(own):
        where += '   [names our faith or a character of ours]'
    elif OURS.search(text):
        where += '   [inside our hook]'
    return 'vanilla', where


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--logs', default=LOGS, help='the game\'s logs folder')
    ap.add_argument('--threshold', type=int, default=95_000, help='warn (or clear) at this many errors')
    ap.add_argument('--interval', type=float, default=10.0, help='seconds between reads')
    ap.add_argument('--auto-clear', action='store_true', help='type Log.ClearErrorLog into the game')
    ap.add_argument('--console-key', default='`', help='the key that opens the console')
    ap.add_argument('--all', action='store_true', help='also keep the whole log')
    args = ap.parse_args()

    src = os.path.join(args.logs, 'error.log')
    os.makedirs(os.path.join(args.logs, 'archive'), exist_ok=True)
    stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    ours_path = os.path.join(args.logs, 'archive', f'ours_{stamp}.log')
    all_path = os.path.join(args.logs, 'archive', f'error_{stamp}.log')
    summary_path = os.path.join(args.logs, 'archive', f'summary_{stamp}.txt')
    if not game_running():
        sys.exit('CK3 is not running. Start the game first, then this script.')
    if args.auto_clear:
        problem = check_auto_clear_access()
        if problem:
            sys.exit(f'--auto-clear cannot work: {problem}\nOr run without --auto-clear and clear the log by hand '
                     'when the script beeps.')
        print('Auto-clear: permissions checked.', flush=True)
    print(f'Keeping the mod\'s errors from {src}\n  -> {ours_path}' + (f'\n  -> {all_path} (everything)' if args.all else '')
          + '\nStops when the game quits. Ctrl-C to stop early.', flush=True)

    vanilla = {}        # the game's own errors by source file
    ours = {}           # the mod's errors kept, by where they were raised
    known = {}          # the mod's harmless errors, by kind
    kept = [0]          # the mod's errors kept
    entry = []          # lines of the entry being read

    def close_entry(out_ours):
        if not entry:
            return
        text = b''.join(entry)
        entry.clear()
        kind, key = classify(text)
        if kind == 'ours':
            out_ours.write(text)
            kept[0] += 1
            ours[key] = ours.get(key, 0) + 1
        elif kind == 'known':
            known[key] = known.get(key, 0) + 1
        else:
            vanilla[key] = vanilla.get(key, 0) + 1

    offset = 0          # bytes of error.log already read
    count = 0           # errors in error.log since the game last cleared it
    total = 0           # errors read this run
    clears = 0
    last_warn = 0.0     # when we last warned about the cap (0: not since the last clear)
    tries = 0           # auto-clear attempts since the last clear
    out_all = open(all_path, 'ab') if args.all else None
    with open(ours_path, 'ab') as out_ours:
        try:
            while True:
                running = game_running()
                try:
                    size = os.path.getsize(src)
                except FileNotFoundError:
                    size = 0
                if size < offset:                       # cleared by the console, or a new game session
                    clears += 1
                    close_entry(out_ours)
                    print(f'{time.strftime("%H:%M:%S")}  error.log was cleared ({clears}); reading from the start',
                          flush=True)
                    mark = f'\n##### error.log cleared at {time.strftime("%H:%M:%S")} #####\n'.encode()
                    out_ours.write(mark)
                    if out_all:
                        out_all.write(mark)
                    offset, count, last_warn, tries = 0, 0, 0.0, 0
                if size > offset:
                    with open(src, 'rb') as f:
                        f.seek(offset)
                        chunk = f.read(size - offset)
                    cut = chunk.rfind(b'\n') + 1         # whole lines only; the rest waits for the next read
                    if cut:
                        chunk = chunk[:cut]
                        offset += cut
                        if out_all:
                            out_all.write(chunk)
                        for line in chunk.splitlines(keepends=True):
                            if HEAD.match(line):
                                close_entry(out_ours)
                            entry.append(line)
                        out_ours.flush()
                        n = chunk.count(ENTRY)
                        count += n
                        total += n
                now = time.time()
                if count >= args.threshold and now - last_warn >= 60:
                    # Warn once a minute until the log is cleared: a failed auto-clear or a missed beep never goes
                    # unnoticed. Auto-clear is tried twice, then left to you.
                    first = last_warn == 0.0
                    last_warn = now
                    lost = ' Logging has STOPPED: errors are being lost.' if count >= CAP else ''
                    if args.auto_clear and tries < 2:
                        tries += 1
                        print(f'\a{time.strftime("%H:%M:%S")}  {count:,} errors: clearing the log '
                              f'(attempt {tries}).{lost}', flush=True)
                        auto_clear(args.console_key)
                    else:
                        why = ('Auto-clear did not clear it. ' if args.auto_clear else '') if not first else ''
                        print(f'\a{time.strftime("%H:%M:%S")}  {count:,} errors (the game stops logging at '
                              f'{CAP:,}). {why}Clear it now: console, Log.ClearErrorLog, Return.{lost}', flush=True)
                if not running:
                    break
                time.sleep(min(args.interval, 3.0) if count >= args.threshold * 0.9 else args.interval)
        except KeyboardInterrupt:
            print('Stopped.', flush=True)
        close_entry(out_ours)
    if out_all:
        out_all.close()
    with open(summary_path, 'w', encoding='utf-8') as v:
        def section(title, d):
            v.write(f'{title} ({sum(d.values()):,} in all):\n')
            for k, n in sorted(d.items(), key=lambda kv: -kv[1]):
                v.write(f'{n:9,}  {k}\n')
            v.write('\n')
        section(f"The mod's errors kept in {os.path.basename(ours_path)}, by where they were raised", ours)
        section("The mod's errors known to be harmless, counted only", known)
        section("The game's own errors, by source", vanilla)
    print(f'Done. {total:,} errors read ({clears} clears): {kept[0]:,} of the mod\'s kept in {ours_path}; '
          f'{sum(known.values()):,} known harmless and the game\'s own counted in {summary_path}.', flush=True)

if __name__ == '__main__':
    main()
