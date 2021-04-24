# Backlog

Working with directories and their contents is a problem that you’ll commonly approach using recursion.

- [] read up on ***recursion***
- [] read up on design, the single responsibility principle.
  


- [] provide a way for your application to take a directory path at the command line.
     - argparse module, from standard python library
- [] use pathlib to provide several tools to manage and represent file system paths.
- [] use python list to store the list of entries in the directory structure
- [] how to shape a good-looking tree diagram that reflects the directory structure in an accurate and user-friendly way and mimics the tree command.


## __init.py

Use __init__.py to turn normal directories into a python package.
Packages contain modules, they are the mechanisms that allow you to organize 
and structure python code.

`__version__ = "0.1.0"` is a python documentation string, commonly known as a docstring.
A docstring defines a global constant called __version__ which holds the application version number.

## nonpublic classes, methods and attributes
The leading underscore character (_) in the name _TreeGenerator is a commonly used Python convention. 
It implies that the class is nonpublic, which means that you don’t expect this class to be used from outside its containing module, rptree.py.