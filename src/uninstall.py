import os
import json
import shutil

pkgname = input('What package do you want to uninstall? ')

os.chdir(os.path.expanduser('~'))
with open(".local/share/pythonpkgs/scripts/% s/pkg-details.json" % pkgname) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
icon = jsonObject['icon']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']

shutil.rmtree('.local/share/pythonpkgs/scripts/% s' % name)
os.remove('.local/share/applications/% s' % desktop)
os.remove('.local/bin/% s.sh' % name)
os.remove('.local/share/icons/hicolor/128x128/apps/% s' % icon)
print('Uninstalling package: % s...' % name, '\033[1m' + 'done.' + '\033[0m')
