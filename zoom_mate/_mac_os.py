

##############################
# Name: Kyle Hurd
# Date: 02/31/2021
# Project: Zoom_Mate
# File: main.py
# Tested: Python3.7
#############################
import os
import time
import pyautogui as py
from AppKit import NSWorkspace
import src.globals as globals
from src.zoom_object import Zoom_Meeting
import src.zoom_object as zm

py.PAUSE = 1


def is_zoom_focused_osx():
    workspace = NSWorkspace.sharedWorkspace()
    return workspace.activeApplication()['NSApplicationName'] == 'zoom.us'


def _join_meeting_osx():
    zm.display_meetings()
    zm.get_meeting_selection()
    meeting = globals.ZOOM_MEETINGS[globals.MEETING_SELECTION - 1]
    if meeting.password == None:
        os.system(
            f'open "zoommtg://zoom.us/join?confno' \
            f'{meeting.meeting_id}'
        )
    else:
        os.system(
            f'open "zoommtg://zoom.us/join?confno=' \
            f'{meeting.meeting_id}?&pwd={meeting.password}"'
            )
    time.sleep(7)
    if not is_zoom_focused_osx():
        _open_zoom_osx()
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/join_with_computer_audio.png',
        confidence = 0.8
    )
    if loc != None:
        py.press('enter')
    return


def _quit_meeting_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    py.hotkey('command', 'W')
    py.press('enter')
    return


def _mute_audio_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/mute_button_on_1.png',
        confidence=0.8
        )
    if loc != None:
        py.hotkey('shift','command','A')
    return


def _unmute_audio_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/mute_button_off.png',
        confidence=0.8
    )
    if loc != None:
        py.hotkey('shift', 'command', 'A')
    return


def _display_video_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/video_off.png',
        confidence=0.8
        )
    if loc != None:
        py.hotkey('shift','command','V')
    return


def _undisplay_video_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/video_on_1.png',
        confidence = 0.8
    )
    if loc != None:
        py.hotkey('shift', 'command', 'V')
    return


def _share_screen_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/share_screen.png',
        confidence = 0.8
    )
    if loc != None:
        py.hotkey('shift','command','S')
        time.sleep(0.5)
        py.press('enter')
    return


def _unshare_screen_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/stop_share.png',
        confidence = 0.8
    )
    if loc != None:
        py.hotkey('shift','command','S')
    return


def _leave_meeting_osx():
    if not is_zoom_focused_osx():
        _open_zoom_osx()
        time.sleep(globals.WAIT_TIME_BETWEEN_COMMANDS)
    loc = py.locateOnScreen(
        globals.IMAGES_LOCATION_MACOS + '/leave_meeting.png',
        confidence = 0.8
    )
    if loc != None:
        py.hotkey('command', 'w')
        py.press('enter')
    else:
        loc = py.locateOnScreen(
            globals.IMAGES_LOCATION_MACOS + '/end_meeting.png',
            confidence = 0.8
        )
        if loc != None:
            py.hotkey('command', 'w')
            py.press('enter')
    return


def _exit_zoom_osx():
    os.system('killall "zoom.us"')
    return


def _open_zoom_osx():
    os.system('open -a "zoom.us"')
    return