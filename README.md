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
 - `create` - create Python Package
    - after creating package, you will get the Tar archive (compressed with zstd), which is the package you created.
 - `install` - install package on your opersting system
 - `uninstall` - uninstall Python package
   - at `uninstall step`, you will still need to type the name of the package you want to uninstall.



  <h3>Tutorial on YouTube</h3>
  <a href=https://www.youtube.com/watch?v=e68fPIFLJFw><img src=https://i9.ytimg.com/vi/e68fPIFLJFw/mqdefault.jpg?v=61ed27c7&sqp=CKTVtI8G&rs=AOn4CLC3mIKOuyoVs2fi8r0NQxFfYSd9YA>


  <h2>License</h2>
  <p>This program is available under</p><a href=https://github.com/vikdevelop/python-packager/blob/main/LICENSE>GPL-3.0 license</a>
