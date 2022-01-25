# PythonPackager
Simple creating, installing, & uninstalling Python (GUI) apps on Linux!

## Usage
1. clone this repo:
```bash
git clone https://github.com/vikdevelop/python-packager.git
```

2. Create *python-package.json* file:
```json
{
  "name": "TYPE YOUR APP NAME",
  "version": "1.0",
  "summary": "SHORT SUMMARY...",
  "script": "yourscript.py",
  "desktop": "filename.desktop",
  "icon": "icon.png/icon.jpg/icon.ico/icon.svg/... with resolution: 128x128"
}
```
3. Run Python script `run.py` :
```bash
chmod +x run.py
./run.py
```
Enter one of three options:
  - `create` - create Python Package from manifest file `python-package.json`
    - in the next step, you will need enter path to your manifest, e.g.: /home/$USER/package_name
  - `install` - install Python Package on your operationg system from package archive (compressed with zstd)
    - in the next step, you wil need enter path to decompressed package archive, e.g.: /home/$USER/package_name
  - `uninstall` - uninstall your python Package from your operating system
    - in the next step, you will need enter package name, want you uninstall.
  - `help` - displays help


  <h2>License</h2>
  <p>This program is available under</p><a href=https://github.com/vikdevelop/python-packager/blob/main/LICENSE>GPL-3.0 license</a>
