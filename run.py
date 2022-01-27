#!/usr/bin/env python
import os

answer = input("What do you want to do (type 'help' for instructions of usage)? ")
if answer == "create":
    os.system("python3 /app/src/pythonpackager.py")
elif answer == "install":
    os.system("python3 /app/src/installer.py")
elif answer == "uninstall":
    os.system("python3 /app/src/uninstall.py")
elif answer == "help":
    print("options:")
    print("- create: Create Python package from manifest file python-package.json")
    print("  - in the next step, you will need type path to package folder, want you create.")
    print("- uninstall: Uninstall Python package from your Operating system")
    print("  - in the next step, you will need type package name, want you uninstall.")
    print("- install: Install your Python Package on your system.")
    print("  - in the next step, you will need type path to package, want you install.")
