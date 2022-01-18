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
os.mkdir("% s" % name)

# Create python script dir
os.makedirs("% s/usr/local/app/scripts" % name)
os.makedirs("% s/usr/bin" % name)
os.makedirs("% s/usr/share/applications" % name)
os.makedirs("% s/usr/share/icons/hicolor/128x128/apps" % name)

# Create runner script
with open('% s.sh' % name, 'w') as f:
    f.write('python3 /usr/local/app/scripts/% s' % script)
pass
print("Runner script =>", '\033[1m' + 'created.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install runner script to /usr/bin
shutil.move('% s.sh' % name, '% s/usr/bin/' % name)
print("% s.sh => installed." % name)
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install .desktop dile
shutil.move('% s' % desktop, '% s/usr/share/applications/' % name)
print("% s =>"  % desktop, '\033[1m' + 'installed.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install icon
shutil.move('% s' % icon, '% s/usr/share/icons/hicolor/128x128/apps/' % name)
print("% s =>" % icon, '\033[1m' + 'installed.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Install Python script(s)
shutil.move('% s' % script, '% s/usr/local/app/scripts/' % name)
print("% s =>" % script, '\033[1m' + 'installed.' + '\033[0m')
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

os.system('cp pkg-details.json ./% s/' % name)
print("Package info file (pkg-details.json) =>", '\033[1m' + 'created.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

# Create Package archive (compressed with zstd)
os.system("tar --zstd -cf % s.pythonpkg.tar.zst % s" % ('name', 'name'))
print("Archive (compressed with zstd) for % s package =>" % name, '\033[1m' + 'compressed.' + '\033[0m')
count_seconds = 1
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #print(i, end='...', flush = True)
        time.sleep(1)
pass

print("Python package was created SUCCESSFULLLY!")
print("Your Python package file is named: % s.pypkg.tar.zst" % name)
