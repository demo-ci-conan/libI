
#include "libI/libI.h"

#include <iostream>

void hello_libI(int indent, const std::string& msg) {
    std::cout << std::string(indent, ' ') << "libI: " << msg << std::endl;
}