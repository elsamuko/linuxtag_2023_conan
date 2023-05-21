#!/usr/bin/env bash

# enable write permission for user demo in server.conf and restart conan_server
# [write_permissions]
# */*@*/*: demo

function green {
    echo -e "\033[1;32m$*\033[0m"
}

function indent {
    sed 's/^/    /'
}

function configure_remote {
    green "configuring conan_server"
    # disable conancenter https://center.conan.io
    conan remote disable conancenter | indent
    # add local conan_server
    conan remote add --insecure --force my_localhost http://localhost:9300 2>&1 | indent
    conan remote list | indent
}

function authenticate_user {
    green "authenticate user 'demo'"
    conan remote login -p demo my_localhost demo | indent
}

function build_and_upload_package {
    green "build and upload package"
    rm -rf server_test | indent
    mkdir -p server_test | indent
    (
        cd server_test || exit 1
        conan new cmake_lib -d name=linuxtag -d version=1.0 2>&1 | indent
        conan create . 2>&1 | indent
    )
    conan upload linuxtag/1.0 -r my_localhost 2>&1 | indent
}

function show_package_on_remote {
    green "show build package on server"
    conan search linuxtag -r my_localhost 2>&1 | indent
}

configure_remote
authenticate_user
build_and_upload_package
show_package_on_remote
