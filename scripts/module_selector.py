#!/usr/bin/python3
from rofi import rofi

from modules import Modules

modules = Modules()
current = modules.current

try:
    current_index = modules.index(current)
    args = ['-a', current_index]
except ValueError:
    args = []

code, index, selected = rofi('Select module', [c.info['title'] for c in modules], [
    '-auto-select',
    '-no-custom',
    '-lines', len(modules)
] + args)

if index >= 0:
    modules.current = modules[index]
