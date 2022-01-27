import os
import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class PythonGUIWindow(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self, title="Python Packager")
        self.set_border_width(60)
        print("Python Packager was running...")

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(mainBox)

        self.progressbar = Gtk.ProgressBar()

        self.spinner = Gtk.Spinner()
        mainBox.pack_start(self.spinner, True, True, 0)

        self.label = Gtk.Label()
        mainBox.pack_start(self.label, True, True, 0)

        self.buttonStart = Gtk.Button(label="Create Package")
        self.buttonStart.connect("clicked", self.on_buttonechopkg_clicked)
        mainBox.pack_start(self.buttonStart, True, True, 0)

        self.buttonStart = Gtk.Button(label="Install Package")
        self.buttonStart.connect("clicked", self.on_buttoninstallpkg_clicked)
        mainBox.pack_start(self.buttonStart, True, True, 0)

        self.buttonStart = Gtk.Button(label="Remove Package")
        self.buttonStart.connect("clicked", self.on_buttonrmpkg_clicked)
        mainBox.pack_start(self.buttonStart, True, True, 0)

    def on_buttonechopkg_clicked(self, widget, *args):
        self.echopkg()

    def on_buttoninstallpkg_clicked(self, widget, *args):
        self.installpkg()

    def on_buttonrmpkg_clicked(self, widget, *args):
        self.rmpkg()

    def echopkg(self):
        command = 'python3 /app/src/pythonpackager.py'
        os.system("gnome-terminal -e 'bash -c \"% s; exec bash\"'" % command)

    def installpkg(self):
        command = 'python3 /app/src/installer.py'
        os.system("gnome-terminal -e 'bash -c \"% s; exec bash\"'" % command)

    def rmpkg(self):
        command = 'python3 /app/src/uninstall.py'
        os.system("gnome-terminal -e 'bash -c \"% s; exec bash\"'" % command)



win = PythonGUIWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
