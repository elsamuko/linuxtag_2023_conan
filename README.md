# linuxtag_2023_conan

Files for the 2023 Linuxtag  
https://docs.conan.io/2/

## Install

* `python3 -m pip install conan`

## Use Packages

* `conan install .`

## Create Packages

* `conan new cmake_lib -d name=linuxtag -d version=1.0`
* `conan create .`
* `conan test test_package linuxtag/1.0`

