#!/usr/bin/env python
import os

answer = input("What do you want to do? ")
if answer == "create":
    os.system("python3 src/pythonpackager.py")
elif answer == "install":
    os.system("sudo python3 src/installer.py")
