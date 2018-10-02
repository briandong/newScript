#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a script to generate new python project '

__author__ = "Bo DONG"

import sys, os

def main():
    if len(sys.argv) == 1:
        print("Please specify the project dir")
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            print("Dir '{}' already exists. Please specify a new dir".format(path))
        else:
            # Get project name
            name = path.split('/')[-1]

            # Create dirs
            print("Creating dir: {}".format(path))
            os.makedirs(path+"/"+name)
            os.makedirs(path+"/tests")
            os.makedirs(path+"/docs")

            # Create files
            header = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a script to do some work '

__author__ = "J Smith"

import sys, os
"""
            # Create script
            body = """
def func():
    return "Hello World!"

def main():
    print(func())

# Only run the following code when this file is the main file being run
if __name__=='__main__':
    main()
"""
            with open(path+"/"+name+"/"+name+".py", "w") as f:
                f.write(header)
                f.write(body)
            
            # Create context
            context_body = """
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '{}')))

import {}
""".format(name, name)
            with open(path+"/tests/context.py", "w") as f:
                f.write(header)
                f.write(context_body)

            # Create test
            test_body = """import unittest

from context import {}

class Test_func(unittest.TestCase):
    def test_func(self):
        self.assertEqual({}.func(), "Hello World!")
""".format(name, name)

            with open(path+"/tests/test_"+name+".py", "w") as f:
                f.write(header)
                f.write(test_body)

            # Create Makefile
            make_body = """
init:
    pip install -U pytest

test:
    pytest

PHONY: init test
"""
            with open(path+"/Makefile", "w") as f:
                f.write(make_body)

            # Create README
            read_body = """
[TOC]

# Introduction

This script can do some work

"""
            with open(path+"/README.md", "w") as f:
                f.write(read_body)

            # Create doc
            with open(path+"/docs/"+name+".md", "w") as f:
                pass

# Only run the following code when this file is the main file being run
if __name__=='__main__':
    main()