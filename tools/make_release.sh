#!/usr/bin/env bash
# Builds a clean copy of the mod for uploading to the Steam Workshop or Paradox Mods.
#
#     tools/make_release.sh [destination]        (default: ~/ck3-crusader-dolls-release)
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

repo="$(cd "$(dirname "$0")/.." && pwd)"
dest="${1:-$HOME/ck3-crusader-dolls-release}"
game_dirs=(common events gfx history localization)

cd "$repo"
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
