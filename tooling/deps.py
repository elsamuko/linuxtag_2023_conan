#!/usr/bin/env python3
# get dependencies from conanfile.py
# conans/test/unittests/client/conanfile_loader_test.py
# conan/cli/commands/graph.py graph_info

import os
import conan.api.conan_api
import conan.api.output
import conans.client.graph.graph
import conans.client.loader
from unittest.mock import MagicMock
import argparse

# silent conan logging
conan.api.output.conan_output_level = conan.api.output.LEVEL_QUIET

# load conanfile.py and get requires
loader = conans.client.loader.ConanFileLoader()
this_dir = os.path.dirname(os.path.realpath(__file__))
conanfile = loader.load_consumer(f"{this_dir}/conanfile.py")
requires = [a.ref for a in list(conanfile.requires.values())]

# dummy to make get_profiles_from_args happy
parser = argparse.ArgumentParser()
parser.add_argument('--profile_host')
parser.add_argument('--profile_build')
parser.add_argument('--settings_build')
parser.add_argument('--options_build')
parser.add_argument('--conf_build')
parser.add_argument('--conf_host')
parser.add_argument('--settings_host')
parser.add_argument('--options_host')
args = parser.parse_args()

# args for load_graph_requires
api = conan.api.conan_api.ConanAPI()
profile_host, profile_build = api.profiles.get_profiles_from_args(args)
remotes = api.remotes.list()

# get all dependencies
deps_graph = api.graph.load_graph_requires(requires=requires,
                                           tool_requires=None,
                                           profile_host=profile_host,
                                           profile_build=profile_build,
                                           lockfile=MagicMock(),
                                           remotes=remotes,
                                           update=False,
                                           check_updates=False)

# print dependencies
for node in deps_graph.nodes:
    if node.context != conans.client.graph.graph.CONTEXT_BUILD and node.ref:
        print(node.ref)
