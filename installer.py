import os
import json
import shutil

print("PYTHONPACKAGER 1.0")

os.mkdir('pkgarchive-decompressed')
os.system('tar xf PACKAGE1.pythonpkg.tar.zst -C ./pkgarchive-decompressed')
print("Archive for this pkg => decompressed.")

with open("pkg-details.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
c1 = jsonObject['c1']
c2 = jsonObject['c2']
c3 = jsonObject['c3']
c4 = jsonObject['c4']

print("Reading data from pkg-details.json file..")

# Installation Package
os.system('cd pkgarchive-decompressed/% s' % name)
print("Running: cd pkgarchive-decompressed/% s" % name)
os.system('% s' % c1)
print("Running: install to /usr/bin/..")
os.system('% s' % c2)
print("Running: install to /usr/local/app/scripts/..")
os.system('% s' % c3)
print("Running: install to /usr/share/applications/..")
os.system('% s' % c4)
print("Running: install to /usr/share/icons/hicolor/128x128/apps/..")

print("Python Package: % s => installed!" % name)
