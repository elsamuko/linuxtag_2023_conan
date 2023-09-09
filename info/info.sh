#!/usr/bin/env bash
# chg: determine package path

conan install . -of conan 2>/dev/null

# hacky hack (https://github.com/conan-io/conan/issues/13306)
PACKAGE_ID="$(conan list 'libcurl/*:*' | sed -n 7p | xargs)"
PACKAGE_PATH="$(conan cache path "libcurl/8.0.1:$PACKAGE_ID")"

echo "Show contents of package path: $PACKAGE_PATH"
ls -l "$PACKAGE_PATH"
