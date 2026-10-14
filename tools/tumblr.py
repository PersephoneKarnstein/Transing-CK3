#!/usr/bin/env python3
"""Tumblr research helper (scrapes the server-rendered ___INITIAL_STATE___ JSON; no API key).

  tumblr.py tag <tag> [--sort top|recent] [--pages 1]     # posts under a tag
  tumblr.py search "<query>" [--pages 1]                  # site search
  tumblr.py blog <blogname> [--pages 1]                   # a blog's recent posts
  tumblr.py post <url>                                    # one post (full body + reblog chain + notes count)

Output: ===== blogName | date | notes | url  then the post's full text (HTML stripped), including reblog trail.
"""
import json, re, sys, html as H, urllib.parse, urllib.request, argparse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "ignore")

def state(htmltext):
    m = re.search(r'<script type="application/json" id="___INITIAL_STATE___"[^>]*>(.*?)</script>', htmltext, re.S)
    if not m: raise SystemExit("no ___INITIAL_STATE___ found (login wall or layout change)")
    return json.loads(H.unescape(m.group(1)))

def strip(s):
    s = re.sub(r"<br\s*/?>", "\n", s); s = re.sub(r"</p>|</li>|</blockquote>|</h\d>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s); return H.unescape(s).strip()

def content_text(blocks):
    out = []
    for b in blocks or []:
        t = b.get("type")
        if t == "text": out.append(b.get("text", ""))
        elif t == "link": out.append(f'[link: {b.get("url","")} {b.get("title","")}]')
        elif t == "image": out.append("[image]")
        elif t == "video": out.append("[video]")
    return "\n".join(out)

def find_posts(obj, acc):
    """walk any structure collecting post-like dicts (have blogName + content or trail)."""
    if isinstance(obj, dict):
        if "blogName" in obj and ("content" in obj or "trail" in obj) and "postUrl" in obj:
            acc.append(obj)
        else:
            for v in obj.values(): find_posts(v, acc)
    elif isinstance(obj, list):
        for v in obj: find_posts(v, acc)

def show(p):
    date = p.get("date", "") or p.get("timestamp", "")
    print(f'===== {p.get("blogName")} | {date} | notes {p.get("noteCount", p.get("notes",""))} | {p.get("postUrl")}')
    tags = p.get("tags") or []
    if tags: print("tags: " + ", ".join(tags))
    for tr in p.get("trail", []) or []:
        bn = (tr.get("blog") or {}).get("name") or tr.get("brokenBlogName", "?")
        txt = content_text(tr.get("content")) or strip(tr.get("contentRaw", ""))
        if txt: print(f"-- {bn}:\n{txt}")
    own = content_text(p.get("content")) or strip(p.get("body", "") or "")
    if own: print(f"-- {p.get('blogName')} (reblog comment / OP):\n{own}")
    print()

def run(url, pages=1):
    seen = set()
    for i in range(pages):
        u = url if i == 0 else url + ("&" if "?" in url else "?") + f"page={i+1}"
        try: st = state(fetch(u))
        except Exception as e: print(f"[page {i+1} failed: {e}]"); break
        acc = []; find_posts(st, acc)
        new = [p for p in acc if p.get("postUrl") not in seen]
        if not new: break
        for p in new: seen.add(p.get("postUrl")); show(p)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tag"); t.add_argument("tag"); t.add_argument("--sort", default="top"); t.add_argument("--pages", type=int, default=1)
    s = sub.add_parser("search"); s.add_argument("q"); s.add_argument("--pages", type=int, default=1)
    b = sub.add_parser("blog"); b.add_argument("name"); b.add_argument("--pages", type=int, default=1)
    p = sub.add_parser("post"); p.add_argument("url")
    ns = ap.parse_args()
    if ns.cmd == "tag": run(f"https://www.tumblr.com/tagged/{urllib.parse.quote(ns.tag)}?sort={ns.sort}", ns.pages)
    elif ns.cmd == "search": run(f"https://www.tumblr.com/search/{urllib.parse.quote(ns.q)}", ns.pages)
    elif ns.cmd == "blog": run(f"https://www.tumblr.com/{urllib.parse.quote(ns.name)}", ns.pages)
    else: run(ns.url, 1)
