import json
import os
import shutil
from datetime import date
import time
import glob

if not glob.glob("*.json"):
    print("No JSON manifest was found. Nothing to do.")
    exit()

today = date.today()

with open("pkg-manifest.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']
mainscript = jsonObject['mainscript']

print('\033[1m' + 'Creation package' + '\033[0m')

# Create dir for prepare compresing to tar.zst archive
if not os.path.exists('package'):
    os.mkdir('package')
    # Create python script dir
    print("Preparing...", '\033[1m' + 'done.' + '\033[0m')
    os.makedirs("package/.local/share/pythonpkgs")
    os.makedirs("package/.local/bin")
    os.makedirs("package/.local/share/applications")
    os.makedirs("package/.local/share/icons/hicolor/128x128/apps")
else:
    shutil.rmtree("package")
    print("Cleaning package directory...", '\033[1m' + 'done.' + '\033[0m')
    print("Preparing...", '\033[1m' + 'done.' + '\033[0m')
    os.makedirs("package/.local/share/pythonpkgs")
    os.makedirs("package/.local/bin")
    os.makedirs("package/.local/share/applications")
    os.makedirs("package/.local/share/icons/hicolor/128x128/apps")
# Create runner script
with open('% s' % name, 'w') as f:
    f.write("#!/usr/bin/python3\n")
    f.write("import os\n")
    f.write("os.system('python3 $HOME/.local/share/pythonpkgs/% s/% s')\n" % (name, mainscript))


os.system('chmod +x % s' % name)
print("Creating: Runner script =>", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)

# Install runner script to .local/bin
shutil.move('% s' % name, 'package/.local/bin/')
print("Installing: runner script =>", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)

# Install .desktop dile
shutil.move('% s' % desktop, 'package/.local/share/applications/')
print("Installing: % s =>"  % desktop, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)


# Install icon
shutil.move('% s' % icon, 'package/.local/share/icons/hicolor/128x128/apps/')
print("Installing: % s =>" % icon, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)


# Install Python script(s)
shutil.move('% s' % script, 'package/.local/share/pythonpkgs/')
print("Installing: % s =>" % script, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)

# Instal Main script
shutil.move('% s' % mainscript, 'package/.local/share/pythonpkgs/')

# Create pkginfo JSON file
with open('pkg-details.json', 'w') as f:
    f.write('{\n')
    f.write('   "name": "% s",\n' % name)
    f.write('   "summary": "% s",\n' % summary)
    f.write('   "version": "% s",\n' % version)
    f.write('   "script": "% s",\n' % script)
    f.write('   "desktop": "% s",\n' % desktop)
    f.write('   "icon": "% s",\n' % icon)
    f.write('   "mainscript": "% s",\n' % mainscript)
    f.write('   "platform": "Linux",\n')
    f.write('   "created": "% s"\n' % today)
    f.write('}')


shutil.move('pkg-details.json', 'package/')
print("Creating: Package info file (pkg-details.json) =>", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)


# Create Package archive (compressed with zstd)
os.system("tar --zstd -cf % s_% s.pythonpkg.tar.zst package" % (name, version))
print("Compressing to archive for package % s =>" % name, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)


print("Package was created SUCCESSFULLLY!")
print("Package file is: % s_% s.pythonpkg.tar.zst" % (name, version))
