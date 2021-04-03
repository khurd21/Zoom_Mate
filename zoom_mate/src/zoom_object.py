

##############################
# Name: Kyle Hurd
# Date: 02/31/2021
# Project: Zoom_Mate
# File: zoom_object.py
# Tested: Python3.7
#############################
import datetime as dt
import src.globals as globals

class Zoom_Meeting:

    def __init__(self,id='',pwd='',n='',st=dt.datetime(1,1,1,0,0),et=dt.datetime(1,1,1,0,0)):
        self.meeting_id = id
        self.password = pwd
        self.class_name = n
        self.start_time = st
        self.end_time = et
        self.days = []
        return

# END OF CLASS

def generate_zoom_meeting_list_from_dictionary(dic):
    globals.ZOOM_MEETINGS = []
    for m in dic['meetings']:
        zm = Zoom_Meeting()
        zm.meeting_id = m['meeting_id']
        zm.password = m['password'] if m['password'] != 'None' else None
        zm.start_time = m['start_time']
        zm.end_time = m['end_time']
        zm.class_name = m['class_name']
        zm.days = [eval(m['days'][key]) for key in m['days']]
        globals.ZOOM_MEETINGS.append(zm)
    return


def display_meetings():
    if globals.ZOOM_MEETINGS == None:
        return
    
    for i, meeting in enumerate(globals.ZOOM_MEETINGS):
        print(
            f'{i+1}.\n' \
            f'Meeting:    {meeting.class_name}\n' \
            f'Start Time: {meeting.start_time}\n' \
            f'End Time:   {meeting.end_time}\n'   \
            )
    return


def get_meeting_selection():
    len_of_meetings = len(globals.ZOOM_MEETINGS)
    if len_of_meetings == 0:
        return

    sel = -1
    while True:
        try:
            sel = int(input('Select the meeting:\n>> '))
            if sel <= len_of_meetings and sel > 0:
                globals.MEETING_SELECTION = sel
                break

            print(f'{sel} value exceeds number of meetings: {len_of_meetings}')
        except ValueError:
            print('ValueError. Enter meeting numer [1, ..., 3].')
        else:
            print('Unkown issue.')
    return sel