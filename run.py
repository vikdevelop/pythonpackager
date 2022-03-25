#!/usr/bin/python3
import os
import argparse
import sys
import json
def pkg_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"dir {path} is not exists. Try entering a different path.")

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="Displays version of Python Packager and Python", action="store_true")
parser.add_argument("-I", "--install", help="Install Python Package to your OS", type=pkg_path)
parser.add_argument("-C", "--create", help="Create Python Package from manifest file python-package.json", type=pkg_path)
parser.add_argument("-R", "--remove", help="Remove Python Package from your OS.", type=str)
parser.add_argument("-L", "--listpkgs", help="Displays installed packages", action="store_true")

args = parser.parse_args()

if args.listpkgs:
    sys.path.append("/app/src/")
    import listpkgs

if args.version:
    print("Version of Python Packager: 1.4")
    print("Version of Python:")
    os.system('python3 --version')

if args.install:
    sys.path.append('/app/src')
    os.chdir(args.install)
    import installer

if args.create:
    sys.path.append('/app/src')
    os.chdir(args.create)
    import packager

if args.remove:
    sys.path.append('/app/src')
    os.chdir(os.path.expanduser('~'))
    if not os.path.exists(".local/share/pythonpkgs/" + args.remove):
        print("Package " + args.remove + " wasn't found.")
        print("Nothing to do.")
        exit()

    os.chdir('.local/share/pythonpkgs/' + args.remove)
    import uninstaller
