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
3. Run Python script `run.py` :
```bash
chmod +x run.py
./run.py
```
Enter one of tree options:
 - `create` - create Python Package
    - after creating package, you will get the Tar archive (compressed with zstd), which is the package you created.
 - `install` - install package on your opersting system
 - `uninstall` - uninstall Python package
   - at `uninstall.py` file, you will still need to type the name of the package you want to uninstall.
## License
This program is available under ![GPL-3.0 license](https://github.com/vikdevelop/python-packager/blob/main/LICENSE).
