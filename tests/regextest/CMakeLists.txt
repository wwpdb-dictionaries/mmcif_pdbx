cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_DISABLE_SOURCE_CHANGES ON)
set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)

project(dict-pack LANGUAGES C)

message(STATUS "Compiler flags " ${CMAKE_CXX_FLAGS})
#set(BUILD_LIBRARY_DIR "${CMAKE_CURRENT_BINARY_DIR}/lib")
#set(CMAKE_LIBRARY_OUTPUT_DIRECTORY  ${BUILD_LIBRARY_DIR})

set(SOURCE_DIR_REGEX "modules/cc-regex/src")
set(INCLUDE_DIR_REGEX "modules/cc-regex/include")
set(SOURCES_REGEX
            "${SOURCE_DIR_REGEX}/regcomp.c"
            "${SOURCE_DIR_REGEX}/regexec.c"
            "${SOURCE_DIR_REGEX}/regerror.c"
            "${SOURCE_DIR_REGEX}/regfree.c")


add_library("regex" OBJECT ${SOURCES_REGEX})
target_include_directories("regex" PUBLIC ${INCLUDE_DIR_REGEX})

add_executable("t_regex" t_regex.c "$<TARGET_OBJECTS:regex>")
target_include_directories("t_regex" PUBLIC ${INCLUDE_DIR_REGEX})
