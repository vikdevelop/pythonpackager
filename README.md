# PythonBuilder
Simple installation Python Apps on Linux!

## Usage
1. clone this repo:
```bash
git clone https://github.com/vikdevelop/python-builder.git
```

2. Create *.json* file:
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
3. Run Python Packager via Linux terminal:
```bash
python3 pythonpackager.sh
```
4. After successfully building package, run script `installer.py` via terminal:
```bash
python3 installer.py
```
