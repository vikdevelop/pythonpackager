#!/usr/bin/env python
import os

answer = input("What do you want to do? ")
if answer == "create":
    os.system("python3 src/pythonpackager.py")
elif answer == "install":
    os.system("sudo python3 src/installer.py")
elif answer == "uninstall":
    os.system("sudo python3 src/uninstall.py")
elif answer == "help":
    print("USAGE:\n")
    print("options:\n")
    print("- create: Create Python package from manifest file python-package.json\n")
    print("- uninstall: Uninstall Python package from your Operationg system\n")
    print("- install: Install your Python Package on your system.")
