import os
import json
import shutil

with open("pkg-details.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
icon = jsonObject['icon']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']

HOME = os.path.expanduser('~')
shutil.rmtree('% s/.local/share/pythonpkgs/scripts/% s' % (HOME, name))
os.remove('% s/.local/share/applications/% s' % (HOME, desktop))
os.remove('% s/.local/bin/% s.sh' % (HOME, name))
os.remove('% s/.local/share/icons/hicolor/128x128/apps/% s' % (HOME, icon))
print('Uninstalling package: % s...' % name, '\033[1m' + 'done.' + '\033[0m')
