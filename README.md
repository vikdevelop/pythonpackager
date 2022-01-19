# PythonPackager
Simple installation Python Apps on Linux!

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
3. Run Bash script `pythonpackager.sh`:
```bash
sh pythonpackager.sh
```
4. Done!

Package was created **successfully!**
## License
This program is available under ![GPL-3.0 license](https://github.com/vikdevelop/python-packager/blob/main/LICENSE).
