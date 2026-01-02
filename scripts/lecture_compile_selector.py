#!/usr/bin/python3
# Handles a GUI menu with compilation options
from modules import Modules
from rofi import rofi
from generate_main import build as compile_all_files

lectures = Modules().current.lectures

commands = ['last', 'prev-last', 'all', 'prev', 'master']
options = ['Current lecture', 'Last two lectures', 'All lectures', 'Previous lectures', 'Master compile']

key, index, selected = rofi('Select view', options, [
    '-lines', 5,
    '-auto-select'
])

if index >= 0:
    command = commands[index]
else:
    command = selected

if command == 'master':
    compile_all_files()
else:
    lecture_range = lectures.parse_range_string(command)
    lectures.update_lectures_in_master(lecture_range)
    lectures.compile_master()
