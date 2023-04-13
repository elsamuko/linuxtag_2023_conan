# https://docs.conan.io/2/tutorial/creating_packages/handle_sources_in_packages.html
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
import conan.tools.files as files
from conan.tools.scm import Git


class linuxtagRecipe(ConanFile):
    name = "linuxtag"
    settings = "os", "compiler", "build_type", "arch"

    def set_version(self):
        git = Git(self, self.recipe_folder)
        tag = git.run("describe --tags")
        build = git.run("describe --long --tags").split('-')[-2]
        self.version = f"{tag}.{build}"
        self.output.info(f"version : {self.version}")

    @property
    def tag(self):
        split = self.version.split(".")
        split.pop()
        return ".".join(split)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def source(self):
        url = f"https://github.com/elsamuko/linuxtag_2023_conan/archive/refs/tags/{self.tag}.tar.gz"
        self.output.info(f"downloading : {url}")
        files.get(self, url, strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="lib_linuxtag")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
