"""This module provides the RP Tree CLI."""
# cli.py

import argparse
import pathlib
import sys


from . import __version__
from .rptree import DirectoryTree


# TODO: build main function
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


# TODO: build parse_cmd_line_arguments function
def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="RP Tree, a directory tree generator",
        epilog="Thanks for using RP Tree!",
    )
    parser.version = f"RP Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()
