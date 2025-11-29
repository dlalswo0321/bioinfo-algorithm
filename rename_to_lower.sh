#!/usr/bin/env bash
set -euo pipefail

# 반드시 repo 루트에서 실행
git config core.ignorecase false

# 파일명 및 디렉토리명 모두 소문자로 바꾸기
git ls-files -z | while IFS= read -r -d '' f; do
  lower=$(echo "$f" | tr 'A-Z' 'a-z')
  if [[ "$f" != "$lower" ]]; then
    git mv "$f" "$lower"
    echo "Renamed: '$f' → '$lower'"
  fi
done

git commit -m "Standardize filenames to lowercase"
