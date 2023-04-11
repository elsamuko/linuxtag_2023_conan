#!/usr/bin/env bash

find . -name CMakeCache.txt -delete
cmake -S . -DCMAKE_BUILD_TYPE=Release
cmake --build .
