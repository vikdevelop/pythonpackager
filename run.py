#!/usr/bin/env python
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="displays version of Python Packager and Python", action="store_true")
parser.add_argument("-I", "--install", help="Install Python Package to your OS", action="store_true")
parser.add_argument("-C", "--create", help="Create Python Package from manifest file python-package.json", action="store_true")
parser.add_argument("-R", "--remove", help="Remove Python Package from your OS.", action="store_true")

args = parser.parse_args()

if args.version:
    print("Version of Python Packager: 1.1")
    print(os.system("python3 --version"))

if args.install:
    os.system("python3 /app/src/installer.py")

if args.create:
    os.system("python3 /app/src/pythonpackager.py")

if args.remove:
    os.system("python3 /app/src/uninstall.py")
