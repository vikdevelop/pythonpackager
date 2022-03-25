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

print('\033[1m' + 'Uninstallation package' + '\033[0m')
print("=====================================================")
print("Package:         Version:         Description:")
print("% s       % s       % s\n" % (name, version, summary))
confirm = input("Would you like to continue? [Y/n]: ")

if confirm == 'n':
    print("Interrupted.")
    exit()

if confirm == 'Y' or 'y':
    HOME = os.path.expanduser('~')
    shutil.rmtree('% s/.local/share/pythonpkgs/% s' % (HOME, name))
    os.remove('% s/.local/share/applications/% s' % (HOME, desktop))
    os.remove('% s/.local/bin/% s' % (HOME, name))
    os.remove('% s/.local/share/icons/hicolor/128x128/apps/% s' % (HOME, icon))
    print('Uninstalling package: % s...' % name, '\033[1m' + 'done.' + '\033[0m')
