from pathlib import Path

CURRENT_MODULE_SYMLINK = Path('~/Documents/uni/source_notes/active_module').expanduser()
CURRENT_MODULE_ROOT = CURRENT_MODULE_SYMLINK.resolve()
CURRENT_MODULE_WATCH_FILE = Path('/tmp/current_module').resolve()
ROOT = Path('/home/ash/Documents/uni/source_notes/Year 1 Semester 1').expanduser()
DATE_FORMAT = '%a %d %b %Y %H:%M'
