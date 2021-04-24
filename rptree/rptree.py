# rptree.py
# application’s main functionalities
# Walk the root directory and build the tree diagram and display the tree diagram


"""This module provides RP Tree main module"""

import os
import pathlib


PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)