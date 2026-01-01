#!/usr/bin/python3
from pathlib import Path
import yaml

from lectures import Lectures
from config import ROOT, CURRENT_MODULE_ROOT, CURRENT_MODULE_SYMLINK, CURRENT_MODULE_WATCH_FILE

class Module():
    def __init__(self, path):
        self.path = path
        self.name = path.stem

        self.info = yaml.load((path / 'info.yaml').open(), Loader=yaml.SafeLoader)
        self._lectures = None

    @property
    def lectures(self):
        if not self._lectures:
            self._lectures = Lectures(self)
        return self._lectures

    def __eq__(self, other):
        if other == None:
            return False
        return self.path == other.path

class Modules(list):
    def __init__(self):
        list.__init__(self, self.read_files())

    def read_files(self):
        module_directories = [x for x in ROOT.iterdir() if x.is_dir()]
        _modules = [Module(path) for path in module_directories]
        return sorted(_modules, key=lambda c: c.name)

    @property
    def current(self):
        return Module(CURRENT_MODULE_ROOT.resolve())

    @current.setter
    def current(self, module):
        CURRENT_MODULE_SYMLINK.unlink()
        CURRENT_MODULE_SYMLINK.symlink_to(module.path)
        CURRENT_MODULE_WATCH_FILE.write_text('{}\n'.format(module.info['short']))
