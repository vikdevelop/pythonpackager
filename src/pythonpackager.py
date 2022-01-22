import json
import os
import shutil
from datetime import date
import time

today = date.today()

print("PYTHONPACKAGER 1.0")
with open("python-package.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

# Create dir for prepare compresing to tar.zst archive
os.mkdir("package")

# Create python script dir
print("Preparing...", '\033[1m' + 'done.' + '\033[0m')
os.makedirs("package/usr/local/app/scripts")
os.makedirs("package/usr/bin")
os.makedirs("package/usr/share/applications")
os.makedirs("package/usr/share/icons/hicolor/128x128/apps")

# Create runner script
with open('% s.sh' % name, 'w') as f:
    f.write('python3 /usr/local/app/scripts/% s/% s' % (name, script))
pass
print("Creating: Runner script =>", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install runner script to /usr/bin
shutil.move('% s.sh' % name, 'package/usr/bin/')
print("Installing: % s.sh =>" % name, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install .desktop dile
shutil.move('% s' % desktop, 'package/usr/share/applications/')
print("Installing % s =>"  % desktop, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install icon
shutil.move('% s' % icon, 'package/usr/share/icons/hicolor/128x128/apps/')
print("Installing: % s =>" % icon, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install Python script(s)
shutil.move('% s' % script, 'package/usr/local/app/scripts/')
print("Installing: % s =>" % script, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Create pkginfo JSON file
with open('pkg-details.json', 'w') as f:
    f.write('{\n')
    f.write('   "name": "% s",\n' % name)
    f.write('   "summary": "% s",\n' % summary)
    f.write('   "version": "% s",\n' % version)
    f.write('   "script": "% s",\n' % script)
    f.write('   "desktop": "% s",\n' % desktop)
    f.write('   "icon": "% s",\n' % icon)
    f.write('   "platform": "Linux",\n')
    f.write('   "created": "% s"\n' % today)
    f.write('}')
pass

shutil.move('pkg-details.json', 'package/')
print("Creating: Package info file (pkg-details.json) =>", '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Create Package archive (compressed with zstd)
os.system("tar --zstd -cf % s_% s.pythonpkg.tar.zst package" % (name, version))
print("Compressing to archive for package % s =>" % name, '\033[1m' + 'done.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

print("Python package was created SUCCESSFULLLY!")
print("Your Python package file is: % s_% s.pythonpkg.tar.zst" % (name, version))
