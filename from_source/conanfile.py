# https://docs.conan.io/2/tutorial/creating_packages/handle_sources_in_packages.html
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
import conan.tools.files as files
from conan.tools.scm import Git


def enable_detailed_requests_logging():
    __import__("http").client.HTTPConnection.debuglevel = 1


class linuxtagRecipe(ConanFile):
    name = "linuxtag"
    settings = "os", "compiler", "build_type", "arch"

    def set_version(self):
        '''version = tag.distance'''
        git = Git(self, self.recipe_folder)
        tag = git.run("describe --tags --abbrev=0")
        distance = git.run("describe --long --tags").split('-')[-2]
        self.version = f"{tag}.{distance}"
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
        '''download sources from github'''
        enable_detailed_requests_logging()
        url = f"https://github.com/elsamuko/linuxtag_2023_conan/archive/refs/tags/{self.tag}.tar.gz"
        sha256 = "d5e8524f1cea0fcf649188a1d68268203e8869fc18ee5d1f82d7a76fa8e2a235"
        self.output.info(f"downloading : {url}")
        files.get(self, url, sha256=sha256, strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="lib_linuxtag")
        cmake.build()

    def package(self):
        self.output.info(f"BUILD FOLDER : {self.build_folder}")
        self.output.info(f"PACKAGE FOLDER : {self.package_folder}")
        files.copy(self, pattern="*.a",
                   src=self.build_folder,
                   dst=f"{self.package_folder}/lib")
        files.copy(self, pattern="*.hpp",
                   src=f"{self.build_folder}/lib_linuxtag",
                   dst=f"{self.package_folder}/include")

    def package_info(self):
        self.cpp_info.libs = files.collect_libs(self)
