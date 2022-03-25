# Python Packager
Simple creating, installing, & uninstalling Python (GUI) apps on Linux!

## Installation & usage
#### Watch a video-tutorial on YT:

<a href="https://youtu.be/WuOrkaiAa5M"><img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fofficialpsds.com%2Fimageview%2Fr0%2F56%2Fr0569p_large.png%3F1521316500&f=1&nofb=1" height=50></a>

1. clone this repo:
```bash
git clone https://github.com/vikdevelop/python-packager.git
```
2. Build & install on your OS
- For build this app, you will need installed `flatpak-builder`.
- If you're installed `flatpak-builder`, you will start build this project:
```bash
flatpak-builder build com.github.vikdevelop.pythonpackager.yaml # cmd for build Python Packager
flatpak-builder build com.github.vikdevelop.pythonpackager.yaml --install --user # cmd for build and install Python Packager on your OS
```

3. Run `pythonpackager` via Linux terminal:
```bash
flatpak run com.github.vikdevelop.pythonpackager -C /path/to # cmd for creaate package from manifest
flatpak run com.github.vikdevelop.pythonpackager -I /path/to # cmd for install package on your OS
flatpak run com.github.vikdevelop.pythonpackager -R pkgname # cmd for remove a package from your OS
```
### Creation package
- create *pkg-manifest.json* file:
```json
{
  "name": "TYPE YOUR APP NAME",
  "version": "1.0",
  "summary": "SHORT SUMMARY...",
  "script": "src # Type src directory",
  "mainscript": "main.py"
  "desktop": "filename.desktop",
  "icon": "icon.png/icon.jpg/icon.ico/icon.svg/... with resolution: 128x128 px"
}
```
- create or include needed files: `appname-or-id.desktop`, and `scriptname-or-appname.py` (it is also possible to create a directory with Python scripts), and app icon in format `png, ico, jpg, jpeg, svg...` in resolution 128x128 PX.
- For create package from manifest, use command: `flatpak run com.github.vikdevelop.pythonpackager -C /path/to`. **DON'T WRITE `/path/to/pkg-manifest.json`, BUT JUST `/PATH/TO`** .

### Installation package
- if you have a package archive `package-name_version.pythonpkg.tar.zst`, you can install a package on your operating system.
- in terminal, you enter command: `flatpak run com.github.vikdevelop.pythonpackager -I /path/to/`. **DON'T WRITE `/path/to/package-name_version.pythonpkg.tar.zst`, BUT JUST `/PATH/TO`** 

### Uninstallation package
- if you want uninstall Python package from your OS, use command: `flatpak run com.github.vikdevelop.pythonpackager -R pkgname`

## Uninstallation Python Packager from your OS
```bash
flatpak remove com.github.vikdevelop.pythonpackager
```

## License
This program is available under [GPL-3.0 license](https://github.com/vikdevelop/python-packager/blob/main/LICENSE)
