# PythonPackager
Simple creating, installing, & uninstalling Python (GUI) apps on Linux!

## Installation & usage
1. clone this repo:
```bash
git clone https://github.com/vikdevelop/python-packager.git
```
2. Build & install on your OS
- For build this app, you will need installed `flatpak-builder`.
- If you installed `flatpak-builder`, you will start build this project:
```bash
mkdir build #if you not created build dir
flatpak-builder build com.github.vikdevelop.pythonpackager.yaml # build this project
flatpak-builder build com.github.vikdevelop.pythonpackager.yaml --install --user # install this project on your OS as flatpak
```

3. Run `pythonpackager` program via terminal:
```bash
flatpak run com.github.vikdevelop.pythonpackager
```
Enter one of three options:
  - `create` - create Python Package from manifest file `python-package.json`
      - create *python-package.json* file:
          ```json
          {
            "name": "TYPE YOUR APP NAME",
            "version": "1.0",
            "summary": "SHORT SUMMARY...",
            "script": "yourscript.py",
            "desktop": "filename.desktop",
            "icon": "icon.png/icon.jpg/icon.ico/icon.svg/... with resolution: 128x128 px"
          }
          ```
      - create or include needed files: `appname-or-id.desktop`, and `scriptname-or-appname.py` (it is also possible to create a directory with Python scripts), and include app icon in format `png, ico, jpg, jpeg, svg...` in resolution 128x128 px.
      - in the next step, you will need enter path to your manifest, e.g.: /home/$USER/package_name in terminal after command to run this app (command is above)
      - **Result:**
      - if the package was created without problems, you should see an archive of your package: `packagename_version.pythonpkg.tar.zst`
  - `install` - install your package on your OS
      - if you have package archive `packagename_version.pythonpkg.tar.zst`, can you install package to your operating system.
      - in terminal after command to run this app, you enter option: `install` & in the next step, enter path to your package archive, e.g.: `/home/$USER/path/to/pkgname`
      - if installer did not encounter any problems, **it means that your package was installed successfully!**
   - `uninstall` - uninstall Python package from your OS
      - if you want uninstall Python package from your OS, enter option: `uninstall` & in the next step, enter package name, want you uninstall.

### Uninstall Python Packager from your OS
```bash
flatpak remove com.github.vikdevelop.pythonpackager
```

  <h2>License</h2>
  <p>This program is available under<a href=https://github.com/vikdevelop/python-packager/blob/main/LICENSE>GPL-3.0 license</a></p>
