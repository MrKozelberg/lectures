cmake_minimum_required(VERSION 3.5)

project(linear_algebra LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(linear_algebra main.cpp)

FIND_PACKAGE(Boost 1.65 COMPONENTS program_options REQUIRED)

target_link_libraries(linear_algebra PUBLIC ${Boost_LIBRARIES})
target_include_directories(linear_algebra SYSTEM PUBLIC ${Boost_INCLUDE_DIR})
