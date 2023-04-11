cmake_minimum_required(VERSION 3.20)
project(linuxtag CXX)

add_library(linuxtag linuxtag.cpp)
set_target_properties(linuxtag PROPERTIES PUBLIC_HEADER "linuxtag.hpp")
