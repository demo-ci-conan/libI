cmake_minimum_required(VERSION 2.8.12)
project(demo-ci-conan)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(HEADERS include/libI/libI_headerOnly.h)

add_library(libI INTERFACE ${HEADERS})
set_target_properties(libI PROPERTIES CXX_STANDARD 17)
target_link_libraries(libI PRIVATE CONAN_PKG::libJ)

target_include_directories(
    libI PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(FILES ${HEADERS}
        DESTINATION ${CMAKE_INSTALL_PREFIX}/include/libI
        PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ)
