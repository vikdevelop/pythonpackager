# PythonBuilder
Simple installation Python Apps on Linux!

## Usage
1. You need clone this repo:
```
git clone https://github.com/vikdevelop/python-builder.git
```
2. Create `python-package.json` file:
```json
{
  "name": "TYPE YOUR APP NAME",
  "version": "1.0",
  "summary": "TYPE SHORT SUMMARY",
  "script": "*.py",
  "desktop": "*.desktop",
  "icon": "*.png/*.svg/*.ico..."
}
```
And type name, version, summary, script, desktop & icon.

3. In the terminal type:
```sh
./pythonbuilder.sh /path/to/python-package.json
```
