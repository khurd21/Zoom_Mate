

##############################
# Name: Kyle Hurd
# Date: 02/31/2021
# Project: Zoom_Mate
# File: globals.py
# Tested: Python3.7
#############################
import platform

import src.json_parser as json_parser
import src.zoom_object as zoom_object


FILE_SETTINGS_LOCATION = './files'
IMAGES_LOCATION_MACOS = './files/img_macos'

# Queue - like behavior for grabbing string of commands
# Any command inside of SELECTION list will be executed on start-up
SETTINGS_DATA = json_parser.retrieve_json(FILE_SETTINGS_LOCATION + '/settings.json')
ZOOM_MEETINGS = zoom_object.generate_zoom_meeting_list_from_dictionary(SETTINGS_DATA)
SELECTION_QUEUE = ['open'] 
MEETING_SELECTION = -1
WAIT_TIME_BETWEEN_COMMANDS = 0.5        # Make this value higher if your computer cannot keep up with commmands
                                        # ONLY FOR WHEN ZOOM IS ALREADY RUNNING 
 
_MAC_OS = True if platform.system() == 'Darwin' else False
_WINDOWS = True if platform.system() == 'Windows' else False
_LINUX = True if platform.system() == 'Linux' else False

import _mac_os

COMMANDS = {
    'undisplay' : (_mac_os._undisplay_video_osx if _MAC_OS 
    else _undisplay_video_win32 if _WINDOWS
    else _undisplay_video_linux if _LINUX 
    else None
    ),
    'display' : (_mac_os._display_video_osx if _MAC_OS 
    else _display_video_win32 if _WINDOWS
    else _display_video_linux if _LINUX 
    else None
    ),
    'mute' : (_mac_os._mute_audio_osx if _MAC_OS 
    else _mute_audio_win32 if _WINDOWS
    else _mute_audio_linux if _LINUX 
    else None
    ),
    'unmute' : (_mac_os._unmute_audio_osx if _MAC_OS 
    else _unmute_audio_win32 if _WINDOWS
    else _unmute_audio_linux if _LINUX 
    else None
    ),
    'share' : (_mac_os._share_screen_osx if _MAC_OS 
    else _share_screen_win32 if _WINDOWS
    else _share_screen_linux if _LINUX 
    else None
    ),
    'unshare' : (_mac_os._unshare_screen_osx if _MAC_OS 
    else _unshare_screen_win32 if _WINDOWS
    else _unshare_screen_linux if _LINUX 
    else None
    ),
    'join' : (_mac_os._join_meeting_osx if _MAC_OS 
    else _join_meeting_win32 if _WINDOWS
    else _join_meeting_linux if _LINUX 
    else None
    ),
    'open' : (_mac_os.open_zoom_osx if _MAC_OS
    else _open_zoom_win32 if _WINDOWS
    else _open_zoom_linux if _LINUX
    else None
    ),
    'leave' : (_mac_os._leave_meeting_osx if _MAC_OS 
    else _leave_meeting_win32 if _WINDOWS
    else _leave_meeting_linux if _LINUX 
    else None
    ),
    'exit' : (_mac_os._exit_zoom_osx if _MAC_OS 
    else _exit_zoom_win32 if _WINDOWS
    else _exit_zoom_linux if _LINUX 
    else None
    )
}