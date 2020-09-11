#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a script to create new python project '

__author__ = "Bo DONG"

import sys, os
import optparse


def main():
    usage = "usage: python %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option('-d', '--dir',
        action="store", dest="target_dir",
        help="target dir", default=None)
    options, args = parser.parse_args()

    print("Arguments:", args)
    print("Target dir:", options.target_dir)

    path = options.target_dir
    if os.path.isdir(path):
        print("Dir '{}' already exists. Please specify a new dir".format(path))
    else:
        # get project name
        name = path.split('/')[-1]

        # ****************
        # create dirs
        # ****************
        print("Creating dir: {}".format(path))
        os.makedirs(path+"/"+name)
        os.makedirs(path+"/tests")
        os.makedirs(path+"/docs")

        # ****************
        # create files
        # ****************
        header = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a script to do work '
__author__ = "Bo DONG"

import sys, os
"""
        footer = """
# only run the following code when this file is the main file being run
if __name__=='__main__':
    main()

"""

        # create script
        body = """
import optparse


def func():
    return "Hello World!"

def main():
    usage = "usage: python %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option('-d', '--dir',
        action="store", dest="target_dir",
        help="target dir", default=None)
    options, args = parser.parse_args()

    print("Arguments:", args)
    print("Target dir:", options.target_dir)

    print(func())

"""
        with open(path+"/"+name+"/"+name+".py", "w") as f:
            f.write(header)
            f.write(body)
            f.write(footer)
        
        # create context
        context_body = """
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '{}')))

import {}
""".format(name, name)
        with open(path+"/tests/context.py", "w") as f:
            f.write(header)
            f.write(context_body)

        # create tests
        test_body = """import unittest

from context import {}

class Test_func(unittest.TestCase):
    def test_func(self):
        self.assertEqual({}.func(), "Hello World!")
""".format(name, name)

        with open(path+"/tests/test_"+name+".py", "w") as f:
            f.write(header)
            f.write(test_body)

        # create Makefile
        make_body = """
init:
    pip install -U pytest

test:
    pytest

PHONY: init test
"""
        with open(path+"/Makefile", "w") as f:
            f.write(make_body)

        # create README and docs
        readme_body = """
[TOC]

# Introduction

This script can do work

"""
        with open(path+"/README.md", "w") as f:
            f.write(readme_body)

        # create docs
        with open(path+"/docs/"+name+".md", "w") as f:
            f.write(readme_body)


# only run the following code when this file is the main file being run
if __name__=='__main__':
    main()