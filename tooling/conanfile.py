#!/usr/bin/env python3
from conan import ConanFile

class ToolingTestConan(ConanFile):
    settings = "build_type"
    requires = "libcurl/8.0.1"
    generators = "CMakeDeps"
