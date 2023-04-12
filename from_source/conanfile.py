from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
import conan.tools.files as files


class linuxtagRecipe(ConanFile):
    name = "linuxtag"
    version = "1.0"

    settings = "os", "compiler", "build_type", "arch"

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        files.get(
            self, "https://codeload.github.com/elsamuko/linuxtag_2023_conan/zip/refs/heads/main")
        cmake = CMake(self)
        cmake.configure(
            build_script_folder="linuxtag_2023_conan-main/lib_linuxtag")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
