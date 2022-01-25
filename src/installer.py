import os
import json
import shutil
import linecache
import time

# warning: before installation package, you will need extract tar.zst archive of your package.

pkgarchive = input("Enter path for package archive, compressed with zstd (e.g.: /home/user/pkg_name): ")

os.chdir('% s/package' % pkgarchive)
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


# Install Bash script
shutil.move('usr/bin/% s.sh' % name, '/usr/bin/')
# Install Desktop file
shutil.move('usr/share/applications/% s' % desktop, '/usr/share/applications/')
# Install App icon
shutil.move('usr/share/icons/hicolor/128x128/apps/% s' % icon, '/usr/share/icons/hicolor/128x128/apps/')

# Create /usr/local/app/scripts directory
if not os.path.exists('/usr/local/app/scripts/% s' % name):
    os.makedirs('/usr/local/app/scripts/% s' % name)
pass

print("Installing Package...", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install Python script(s)
shutil.move('usr/local/app/scripts/% s' % script, '/usr/local/app/scripts/% s/' % name)
shutil.move('pkg-details.json', '/usr/local/app/scripts/% s/' % name)

print("Python Package: % s => installed SUCCESSFULLY!" % name)
