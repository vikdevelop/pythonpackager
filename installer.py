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
summary = jsonObject['summary']
version = jsonObject['version']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

print("Reading data from pkg-details.json file...")
print("Installing Package...")

# Installation Package
os.chdir('pkgarchive-decompressed/% s' % name)
shutil.move('usr/bin/% s.sh' % name, '/usr/bin/')
shutil.move('usr/share/applications/% s' % desktop, '/usr/share/applications/')
shutil.move('usr/share/icons/hicolor/128x128/apps/% s' % icon, '/usr/share/icons/hicolor/128x128/apps/')
os.makedirs('/usr/local/app/scripts')
shutil.move('usr/local/app/scripts/% s' % script, '/usr/local/app/scripts/')

print("Cleaning unnecessary files and directories...")

os.system('cd')
os.system('rm -rf ./pkgarchive-decompressed')
os.system('rm ./pkg-details.json')
os.system('rm -rf ./% s' % name)
print("Python Package: % s => installed!" % name)
