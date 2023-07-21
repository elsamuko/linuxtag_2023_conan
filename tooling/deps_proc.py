#!/usr/bin/env python3
# equivalent to
# conan graph info conanfile.py -f json 2> /dev/null | jq '.nodes[] | select(.context == "host") | select(.ref != "") | .ref'

import os
import json
import subprocess as sp


def run(command: str):
    proc = sp.run(command.split(),
                  stdout=sp.PIPE,
                  stderr=sp.PIPE)
    return proc.stdout.decode()


this_dir = os.path.dirname(os.path.realpath(__file__))
rv = run(f"conan graph info -f json {this_dir}/conanfile.py")
as_json = json.loads(rv)
nodes = as_json["graph"]["nodes"]

for key in nodes:
    node = nodes[key]
    if node["context"] == "host" and node["ref"]:
        print(node["label"])
