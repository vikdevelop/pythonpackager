import json
import os
import shutil

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

# Create dir for prepare compresing to tar.zst file
os.mkdir("% s" % name)

# Create python dirs
os.makedirs("% s/usr/local/app/scripts" % name)
os.makedirs("% s/usr/bin" % name)
os.makedirs("% s/usr/share/applications" % name)
os.makedirs("% s/usr/share/icons/hicolor/128x128/apps" % name)


# Create runner script
with open('% s.sh' % name, 'w') as f:
    f.write('python3 /usr/local/app/scripts/% s' % script)
pass
print("Runner script => created.")

# Install runner script to /usr/bin
shutil.move('% s.sh' % name, '% s/usr/bin/' % name)
print("% s.sh => installed." % name)

# Install .desktop dile
shutil.move('% s' % desktop, '% s/usr/share/applications/' % name)
print("% s => installed." % desktop)

# Install icon
shutil.move('% s' % icon, '% s/usr/share/icons/hicolor/128x128/apps/' % name)
print("% s => installed" % icon)

# Install Python script(s)
shutil.move('% s' % script, '% s/usr/local/app/scripts/' % name)
print("% s => installed" % script)


# Create Package archive (compressed with zstd)
os.system("tar -czvf Package1.pypkg.tar.gz % s" % name)
print("Archive (tar.gz) for % s package => created." % name)

print("Python package was created successfully!!")
print("Your Python package file is named: % s.pypkg.tar.gz" % name)
