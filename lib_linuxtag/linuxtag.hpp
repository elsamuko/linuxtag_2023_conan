#pragma once

#include <string>

#ifdef _WIN32
  #define LINUXTAG_EXPORT __declspec(dllexport)
#else
  #define LINUXTAG_EXPORT
#endif

namespace linuxtag {
    LINUXTAG_EXPORT std::string hello();
}
