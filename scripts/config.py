from pathlib import Path

CURRENT_COURSE_SYMLINK = Path('~/Documents/uni/current_course').expanduser()
CURRENT_COURSE_ROOT = CURRENT_COURSE_SYMLINK.resolve()
CURRENT_COURSE_WATCH_FILE = Path('/tmp/current_course').resolve()
ROOT = Path('/home/ash/Documents/uni/Year 1 Semester 1').expanduser()
DATE_FORMAT = '%a %d %b %Y %H:%M'
