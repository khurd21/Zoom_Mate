

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
import zoom_object as zm

from config import Config
from .base_object import ZoomObject

py.PAUSE = 0.5
ZOOM_APP     = 'zoom.us'
TERMINAL_APP = 'terminal'




class _MAC_OS(ZoomObject):

    def __init__(self, config=Config):
        super().__init__(config=config)


    def is_focused(target) -> bool:
        return NSWorkspace.sharedWorkspace() \
            .activeApplication()['NSApplicationName'] \
                .lower() == target.lower()


    def open_app(self, app):
        os.system(f'open -a "{app}"')


    def REMOVEopen_zoom(self):
        if not self.is_zoom_focused():
            os.system('open -a "zoom.us"')
        while 'zoom.us' not in [x.localizedName() for x in NSWorkspace.sharedWorkspace().runningApplications()]:
            time.sleep(2)
        return


    def _exit_zoom(self):
        os.system('killall "zoom.us"')
        exit()


    def _join_meeting(self):
        zm.get_meeting_selection() ### USE SELF.MEETINGS
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
        if not self.is_zoom_focused():
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            globals.IMAGES_LOCATION_MACOS + '/join_with_computer_audio.png',
            confidence = 0.8
        )
        if loc != None:
            py.press('enter')
        return


    def _quit_meeting(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        py.hotkey('command', 'W')
        py.press('enter')
        return


    def _mute_audio(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/mute_button_on_1.png',
            confidence=0.8
            )
        if loc != None:
            py.hotkey('shift','command','A')
        return


    def _unmute_audio(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/mute_button_off.png',
            confidence=0.8
        )
        if loc != None:
            py.hotkey('shift', 'command', 'A')
        return


    def _display_video(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/video_off.png',
            confidence=0.8
            )
        if loc != None:
            py.hotkey('shift','command','V')
        return


    def _undisplay_video(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/video_on_1.png',
            confidence = 0.8
        )
        if loc != None:
            py.hotkey('shift', 'command', 'V')
        return


    def _share_screen(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/share_screen.png',
            confidence = 0.8
        )
        if loc != None:
            py.hotkey('shift','command','S')
            time.sleep(0.5)
            py.press('enter')
        return
    
    
    def _unshare_screen(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/stop_share.png',
            confidence = 0.8
        )
        if loc != None:
            py.hotkey('shift','command','S')
        return
    
    
    def _leave_meeting(self):
        if not self.is_focused(ZOOM_APP):
            self.open_app(ZOOM_APP)
            time.sleep(self._config.WAIT_TIME_BETWEEN_COMMANDS)
        loc = py.locateOnScreen(
            self._config.IMG_PATH + '/leave_meeting.png',
            confidence = 0.8
        )
        if loc != None:
            py.hotkey('command', 'w')
            py.press('enter')
        else:
            loc = py.locateOnScreen(
                self._config.IMG_PATH + '/end_meeting.png',
                confidence = 0.8
            )
            if loc != None:
                py.hotkey('command', 'w')
                py.press('enter')
        return
    
    
    def _start_new_meeting(self):
        pass
