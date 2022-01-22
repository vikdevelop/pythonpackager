import os
import json
import shutil

pkgname = input('What package do you want to uninstall? ')

with open("/usr/local/app/scripts/% s/pkg-details.json" % pkgname) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
icon = jsonObject['icon']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']

shutil.rmtree('/usr/local/app/scripts/% s' % name)
os.remove('/usr/share/applications/% s' % desktop)
os.remove('/usr/bin/% s.sh' % name)
os.remove('/usr/share/icons/hicolor/128x128/apps/% s' % icon)
print('Uninstalling package: % s...' % name, '\033[1m' + 'done.' + '\033[0m')
