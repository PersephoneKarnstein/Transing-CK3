#!/usr/bin/env bash
# Builds a clean copy of the mod for uploading to the Steam Workshop or Paradox Mods.
#
#     tools/make_release.sh [destination]        (default: ~/ck3-crusader-dolls-release)
#     tools/make_release.sh --upload "change note" [destination]
#
# --upload also publishes the release to the Workshop item below, through the running Steam client, with the given
# change note. It uses the Steamworks bridge bundled with the Paradox Modding Toolkit's VS Code extension
# (jdeffner.px-toolkit), run with node; the Paradox Launcher is not involved. It updates only the item's files and
# change note: the title, description, tags, preview and visibility on the Workshop page are left as they are.
#
# The Paradox Launcher uploads every file in the mod's folder, so the repository itself must never be uploaded:
# it holds .git, tools/, docs/ and, on a working machine, the gitignored research folders (raw scrapes, book text,
# private posts). This copies only the folders the game reads, and only the files git tracks in them, plus
# descriptor.mod and thumbnail.png.
#
# WARNING: right after the first upload (2026-10-21) the launcher deleted every local mod of the same name,
# including the folder of the dev launcher entry, which was this repository. Push before uploading, and never
# point a launcher .mod file at the repository while uploading.
#
# The Workshop id lives only in the release copy's descriptor (below), never in the repository's: a dev copy that
# claims the Workshop id is liable to be "updated" over by the launcher.
set -euo pipefail

workshop_id="3823772597"		# https://steamcommunity.com/sharedfiles/filedetails/?id=3823772597

upload=""
note=""
if [ "${1:-}" = "--upload" ]; then
	upload=1
	note="${2:-}"
	[ -n "$note" ] || { echo "--upload needs a change note: tools/make_release.sh --upload \"what changed\"" >&2; exit 1; }
	shift 2
fi

repo="$(cd "$(dirname "$0")/.." && pwd)"
dest="${1:-$HOME/ck3-crusader-dolls-release}"
game_dirs=(common events gfx history localization)

cd "$repo"
# Releases come from master only: work in progress lives on other branches (v2-1066, the 1066 start) until it is ready.
branch="$(git rev-parse --abbrev-ref HEAD)"
if [ "$branch" != "master" ]; then
	echo "On branch '$branch': releases are made from master only (git switch master)." >&2
	exit 1
fi
if [ -n "$(git status --porcelain -- "${game_dirs[@]}" descriptor.mod thumbnail.png)" ]; then
	echo "Uncommitted changes in the mod's files; commit them first so the release matches the repository:" >&2
	git status --short -- "${game_dirs[@]}" descriptor.mod thumbnail.png >&2
	exit 1
fi
if [ -n "$(git log --oneline '@{u}..' 2>/dev/null)" ]; then
	echo "Unpushed commits: push before uploading (the launcher has deleted local mod folders after an upload)." >&2
	exit 1
fi
case "$dest" in
	"$repo"|"$repo"/*) echo "The release must not be inside the repository." >&2; exit 1 ;;
esac

rm -rf "$dest"
mkdir -p "$dest"
git ls-files -z -- "${game_dirs[@]}" | while IFS= read -r -d '' f; do
	mkdir -p "$dest/$(dirname "$f")"
	cp -p "$f" "$dest/$f"
done
cp -p thumbnail.png "$dest/"
grep -vE '^remote_file_id=' descriptor.mod > "$dest/descriptor.mod"
printf 'remote_file_id="%s"\n' "$workshop_id" >> "$dest/descriptor.mod"

# Nothing outside the game's folders, and nothing from the research notes, may be in the release.
if find "$dest" \( -name '.git' -o -name '.DS_Store' -o -path '*/docs/*' -o -path '*/tools/*' -o -name 'web_*.md' \) | grep -q .; then
	echo "Release contains files it must not; aborting." >&2
	exit 1
fi

echo "Release written to $dest ($(git ls-files -- "${game_dirs[@]}" | wc -l | tr -d ' ') files, $(du -sh "$dest" | cut -f1))."
echo "Version $(grep -E '^version=' descriptor.mod | cut -d'"' -f2), commit $(git rev-parse --short HEAD), Workshop item $workshop_id."

[ -n "$upload" ] || exit 0

# Publish through the Steam client (see the header).
ext="$(ls -d "$HOME"/.vscode/extensions/jdeffner.px-toolkit-* 2>/dev/null | sort -V | tail -1)"
[ -n "$ext" ] && [ -f "$ext/dist/steamBridge.js" ] || { echo "The Paradox Modding Toolkit VS Code extension (jdeffner.px-toolkit) is not installed." >&2; exit 1; }
command -v node >/dev/null || { echo "node is not on PATH." >&2; exit 1; }
pgrep -qf 'Steam.app|steam_osx' || { echo "Start the Steam client first: the upload goes through it." >&2; exit 1; }

job="$(python3 -c 'import json,sys; print(json.dumps({"action":"publish","appId":1158310,"itemId":sys.argv[1],"submits":[{"contentPath":sys.argv[2],"changeNote":sys.argv[3]}]}))' "$workshop_id" "$dest" "$note")"
echo "Uploading to Workshop item $workshop_id..."
status=0
printf '%s' "$job" | node "$ext/dist/steamBridge.js" "$ext/dist/steamwand" 2>/dev/null | python3 -c '
import json, sys
ok = False
for line in sys.stdin:
    line = line.strip()
    if not line.startswith("{"):
        continue
    e = json.loads(line)
    if e.get("type") == "progress":
        total = e.get("total") or 0
        pct = " %d%%" % (100 * e.get("uploaded", 0) // total) if total else ""
        print("  " + str(e.get("status")) + pct, flush=True)
    elif e.get("type") == "error":
        print("Upload failed: " + e.get("message", "?"), file=sys.stderr)
    elif e.get("type") == "done":
        ok = True
        print("Published: https://steamcommunity.com/sharedfiles/filedetails/?id=" + e["result"]["itemId"])
        if e["result"].get("needsToAcceptAgreement"):
            print("Steam asks you to accept the Workshop legal agreement before the update shows.")
sys.exit(0 if ok else 1)
' || status=$?
exit $status
