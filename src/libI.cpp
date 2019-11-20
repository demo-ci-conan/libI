
#include "libI/libI.h"

#include <iostream>
#include "libA/libA.h"

void hello_libI(int indent, const std::string& msg) {
    std::cout << std::string(indent, ' ') << "libI: " << msg << std::endl;
    hello_libA(indent+1, "hello from libI");
}