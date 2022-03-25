import os
import json
import shutil
import time
import glob

if not glob.glob('*.tar.zst'):
    print("No package archive was found. Nothing to do.")
    exit()

os.system("tar -xf *.tar.zst")

os.chdir("package")
with open("pkg-details.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
summary = jsonObject['summary']
version = jsonObject['version']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

print('\033[1m' + 'Installation package' + '\033[0m')
print("=====================================================")
print("Package:         Version:         Description:")
print("% s       % s       % s\n" % (name, version, summary))
yesno = input("Would you like to continue? [Y/n]: ")

if yesno == 'n':
    print("Interrupted.")
    exit()

if yesno == 'Y' or 'y':
    HOME = os.path.expanduser('~')

    if not os.path.exists("% s/.local/bin" % HOME):
        os.makedirs("% s/.local/bin" % HOME)
    else:
        print("Package % s is installed." % name)
        print("Nothing to do.")
        exit()

    if not os.path.exists("% s/.local/share/icons/hicolor/128x128/apps" % HOME):
        os.makedirs("% s/.local/share/icons/hicolor/128x128/apps" % HOME)

    if not os.path.exists("% s/.local/share/applications" % HOME):
        os.makedirs("% s/.local/share/applications" % HOME)

    print("Reading data from pkg-details.json file...", '\033[1m' + 'done.' + '\033[0m')
    count_seconds = 1
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            #print(i, end='...', flush = True)
            time.sleep(1)

    # Install runner script
    shutil.move('.local/bin/% s' % name, '% s/.local/bin/' % HOME)
    # Install Desktop file
    shutil.move('.local/share/applications/% s' % desktop, '% s/.local/share/applications/' % HOME)
    # Install App icon
    shutil.move('.local/share/icons/hicolor/128x128/apps/% s' % icon, '% s/.local/share/icons/hicolor/128x128/apps/' % HOME)

    # Create /usr/local/app/scripts directory
    if not os.path.exists('% s/.local/share/pythonpkgs/% s' % (HOME, name)):
        os.makedirs('% s/.local/share/pythonpkgs/% s' % (HOME, name))


    print("Installing Package...", '\033[1m' + 'done.' + '\033[0m')
    count_seconds = 1
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            #print(i, end='...', flush = True)
            time.sleep(1)


    # Install Python script(s)
    shutil.move('.local/share/pythonpkgs/% s' % script, '% s/.local/share/pythonpkgs/% s/' % (HOME, name))
    # Install pkg-details.json file
    shutil.move('pkg-details.json', '% s/.local/share/pythonpkgs/% s/' % (HOME, name))

    print("Package % s was installed successfully!" % name)
    print("Try run package with command: $HOME/.local/bin/% s or % s" % (name, name))
