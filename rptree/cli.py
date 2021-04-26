"""This module provides the RP Tree CLI."""
# cli.py

import argparse
import pathlib
import sys


from . import __version__
from .rptree import DirectoryTree


def main():
    # TODO: build parse_cmd_line_arguments() function
    args = parse_cmd_line_arguments()
    # turn root_dir into a pathlib object
    root_dir = pathlib.Path(args.root_dir)
    # TODO: if not root_dir.is_dir(): how to avoid sys.exit() or why do we need to do sys.exit()?
    # check if root_dir is a valid directory
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    # TODO: build tree object and generate tree with .generate()
    tree = DirectoryTree(root_dir)
    tree.generate()
