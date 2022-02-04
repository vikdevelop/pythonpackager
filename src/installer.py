import os
import json
import shutil
import time
import sys

# warning: before installation package, you will need extract tar.zst archive of your package.

print("PYTHONPACKAGER 1.0")

with open("pkg-details.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
summary = jsonObject['summary']
version = jsonObject['version']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

print("Reading data from pkg-details.json file...", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass
# cd home folder
os.chdir(os.path.expanduser('~'))

# Install Bash script
shutil.move('% s/package/.local/bin/% s.sh' % (pkgarchive, name), '.local/bin/')
# Install Desktop file
shutil.move('% s/package/.local/share/applications/% s' % (pkgarchive, desktop), '.local/share/applications/')
# Install App icon
shutil.move('% s/package/.local/share/icons/hicolor/128x128/apps/% s' % (pkgarchive, icon), '.local/share/icons/hicolor/128x128/apps/')

# Create /usr/local/app/scripts directory
if not os.path.exists('.local/share/pythonpkgs/scripts/% s' % name):
    os.makedirs('.local/share/pythonpkgs/scripts/% s' % name)
pass

print("Installing Package...", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install Python script(s)
shutil.move('% s/package/.local/share/pythonpkgs/scripts/% s' % (pkgarchive, script), '.local/share/pythonpkgs/scripts/% s/' % name)
shutil.move('% s/package/pkg-details.json' % pkgarchive, '.local/share/pythonpkgs/scripts/% s/' % name)

print("Python Package: % s => installed SUCCESSFULLY!" % name)
