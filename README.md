# linuxtag_2023_conan

Files for the 2023 Linuxtag  
https://docs.conan.io/2/

## Install

* `python3 -m pip install conan`

## Use Packages

* `conan install .`

### Info

* `conan graph info .`
* `conan graph info --requires boost/1.81.0`
* `conan graph info . -f dot | dot -Tpng -o out.png`
* `conan list 'libcurl/*:*'` -> PACKAGE_ID
* `conan cache path libcurl/8.0.1:$PACKAGE_ID`

## Create Packages

* `conan new cmake_lib -d name=linuxtag -d version=1.0`
* `conan create .`
* `conan list linuxtag`
* `conan test test_package linuxtag/1.0`

### From 3rd party source

* [tools](https://docs.conan.io/2/examples/tools.html)
* `conan create .`

## Tooling

* with API
* with subprocess

## Server

* `python3 -m pip install conan-server`
* run with `conan_server`
