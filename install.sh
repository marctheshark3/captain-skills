#!/bin/sh
# Link or copy skills into the personal OpenCode skills dir.
# Does not touch the project you are being paid to change.
set -eu

ROOT=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
DEST="${HOME}/.config/opencode/skills"
MODE=link

if [ "${1:-}" = "--copy" ]; then
  MODE=copy
  shift
fi
if [ "${1:-}" != "" ]; then
  DEST=$1
fi

mkdir -p "$DEST"

for dir in "$ROOT"/skills/*; do
  [ -d "$dir" ] || continue
  name=$(basename "$dir")
  target="$DEST/$name"
  if [ "$MODE" = "copy" ]; then
    rm -rf "$target"
    cp -R "$dir" "$target"
  else
    ln -sfn "$dir" "$target"
  fi
  echo "$MODE $name -> $target"
done

echo "Open a new OpenCode session. A running session will not see these."
