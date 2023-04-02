cmake_minimum_required(VERSION 3.20)
project(boost_test CXX)

message("CMAKE_PREFIX_PATH : ${CMAKE_CURRENT_LIST_DIR}/build/conan")
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_CURRENT_LIST_DIR}/build/conan")

find_package(Boost REQUIRED)

add_executable(${PROJECT_NAME} src/test.cpp)
target_link_libraries(${PROJECT_NAME} Boost::unit_test_framework)
