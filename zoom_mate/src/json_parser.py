

##############################
# Name: Kyle Hurd
# Date: 02/31/2021
# Project: Zoom_Mate
# File: json_parser.py
# Tested: Python3.7
#############################
import json
import src.globals as globals

def retrieve_json():
    # We must iterate w/ for loop
    with open(
        globals.FILE_SETTINGS_LOCATION + '/settings.json'
        ) as f_:
        data = json.load(f_)
    return data