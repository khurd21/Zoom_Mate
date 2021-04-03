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

    while True:
        selection = input('>> ').strip().lower().split()
        for sel in selection: 
            if sel in globals.COMMANDS:
                globals.COMMANDS[sel]()
            if sel == 'exit':
                quit()


elif operating_system == 'Linux':
    pass


elif operating_system == 'Windows':
    pass