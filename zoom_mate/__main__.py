#!/usr/bin/env python3

import platform
import src.globals as globals
import src.json_parser as js
from src.zoom_object import Zoom_Meeting
import src.zoom_object as zo


data = js.retrieve_json()
zo.generate_zoom_meeting_list_from_dictionary(data)
del data

operating_system = platform.system()
if operating_system == 'Darwin':

    from _mac_os import is_terminal_focused_osx, _open_terminal_osx

    while True:
        while len(globals.SELECTION_QUEUE) != 0:
            if globals.SELECTION_QUEUE[0] in globals.COMMANDS:
                globals.COMMANDS[globals.SELECTION_QUEUE[0]]()
            globals.SELECTION_QUEUE.pop(0)

        if not is_terminal_focused_osx():
            _open_terminal_osx()

        globals.SELECTION_QUEUE = input('>> ').strip().lower().split()


elif operating_system == 'Linux':
    pass


elif operating_system == 'Windows':
    pass