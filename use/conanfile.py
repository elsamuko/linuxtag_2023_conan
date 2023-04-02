#!/usr/bin/env python3
from conan import ConanFile

class BoostTestConan(ConanFile):
    settings = "build_type"
    requires = "boost/1.81.0"
    generators = "CMakeDeps"
