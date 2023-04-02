#!/usr/bin/env bash

function red  {
    echo -e "\033[1;31m$*\033[0m"
}

function indent {
    sed  's/^/    /'
}

echo
red "generate profile"
conan profile detect 2>&1 | indent

rm -rf build
mkdir -p build
cd build || exit

echo
red "install boost"
conan install .. -of conan -s compiler.version=13 2>&1 | indent

echo
red "configure & build"
find . -name CMakeCache.txt -delete
cmake -S .. -DCMAKE_BUILD_TYPE=Release 2>&1 | indent
cmake --build . 2>&1 | indent

echo
red "run exe"
./boost_test --log_level=test_suite 2>&1 | indent
echo
