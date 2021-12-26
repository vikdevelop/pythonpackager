import json
import os
import shutil

print("PYTHON BUILDER 1.0")
with open("python-package.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

# Create python script dir
os.makedirs("/usr/local/py_apps/scripts")

# Create runner script
with open('% s.sh' % name, 'w') as f:
    f.write('python3 /usr/local/py_apps/scripts/% s' % script)
pass
print("Runner script was created")

# Install runner script to /usr/bin
shutil.move('% s.sh' % name, '/usr/bin')
print("% s.sh has been installed" % name)

# Install .desktop dile
shutil.move('% s' % desktop, '/usr/share/applications')
print("% s has been installed" % desktop)

# Install icon
shutil.move('% s' % icon, '/usr/share/icons/hicolor/128x128/apps')
print("% s has been installed" % icon)

# Install Python script(s)
shutil.move('% s' % script, '/usr/local/py_apps/scripts')
print("% s has been installed" % script)

print("Python App was installed successfully!")
