import json
import os
import shutil

print("PYTHONBUILDER 1.0")
with open("% s/PythonBuilder/python-package.json" % os.environ['HOME']) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

name = jsonObject['name']
version = jsonObject['version']
summary = jsonObject['summary']
script = jsonObject['script']
desktop = jsonObject['desktop']
icon = jsonObject['icon']

# Create python script dir
os.makedirs("% s/.local/py_apps/scripts" % os.environ['HOME'])

# Create runner script
with open('% s.sh' % name, 'w') as f:
    f.write('python3 ./.local/share/py_apps/scripts/% s' % script)
pass
print("Runner script was created")

# Install runner script to /usr/bin
shutil.move('% s.sh' % name, '% s/.local/bin' % os.environ['HOME'])
print("% s.sh has been installed" % name)

# Install .desktop dile
shutil.move('% s' % desktop, '% s/.local/share/applications' % os.environ['HOME'])
print("% s has been installed" % desktop)

# Install icon
shutil.move('% s' % icon, '% s/.local/share/icons/hicolor/128x128/apps' % os.environ['HOME'])
print("% s has been installed" % icon)

# Install Python script(s)
shutil.move('% s' % script, '% s/.local/share/py_apps/scripts' % os.environ['HOME'])
print("% s has been installed" % script)

print("Python App was installed successfully!")
print("You can run your Python application using the command: sh ./.local/bin/% s.sh" % name)
