#include "linuxtag.hpp"
#include <iostream>

#define LOG( A ) std::cout << A << std::endl;

int main( int argc, char* argv[] ) {
    LOG( linuxtag::hello() );
    return 0;
}

