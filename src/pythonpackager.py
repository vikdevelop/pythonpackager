import os
import json
import shutil
import linecache

print("PYTHONPACKAGER 1.0")

os.chdir('package')
"""
# Uncomment this lines, if you need to extract archive of this package. You can also use the following command to extract package (type it into a Linux terminal (or console)):
# tar xf name_version.pythonpkg.tar.zst -C ./
"""
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

# Install Python script(s)
shutil.move('usr/local/app/scripts/% s' % script, '/usr/local/app/scripts/% s/' % name)
shutil.move('pkg-details.json', '/usr/local/app/scripts/% s/' % name)

print("Python Package: % s => installed SUCCESSFULLY!" % name)
