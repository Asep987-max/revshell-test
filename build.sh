#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

rm -rf build dist *.egg-info
python3 -m pip install --upgrade build twine >/dev/null
python3 -m build
python3 -m twine check dist/*
echo "--- artifacts ---"
ls -lh dist/
echo
echo "publish:  python3 -m twine upload dist/*"
