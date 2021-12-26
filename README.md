# PythonBuilder
Simple installation Python Apps on Linux!

## Usage
1. clone this repo:
```
git clone https://github.com/vikdevelop/python-builder.git
```
2. Create PythonBuilder directory in your Home Folder
```sh
mkdir ./PythonBuilder
```
3. Create *.json* file in ./PythonBuilder dir
```json
{
  "name": "TYPE YOUR APP NAME",
  "version": "1.0",
  "summary": "sHORT SUMMARY...",
  "script": "yourscript.py",
  "desktop": "filename.desktop",
  "icon": "icon.png/icon.jpg/icon.ico/icon.svg/..."
}
```
4. Run Python Builder Bash script:
```sh
sudo sh pythonbuilder.sh
```
