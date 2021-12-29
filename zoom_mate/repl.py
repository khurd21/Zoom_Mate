from config import Config
from .zoom_object import generate_object


def _get_commands(zoom_object):
    return {
    'undisplay' : zoom_object._undisplay_video,
    'display'   : zoom_object._display_video,
    'mute'      : zoom_object._mute_audio,
    'unmute'    : zoom_object._unmute_audio,
    'share'     : zoom_object._share_screen,
    'unshare'   : zoom_object._unshare_screen,
    'join'      : zoom_object._join_meeting,
    'leave'     : zoom_object._leave_meeting,
    'open'      : zoom_object._open_zoom,
    'exit'      : zoom_object._exit_zoom,
    }


SELECTION_QUEUE = ['open']
def repl(zoom_object=None, config=Config):

    if zoom_object is None:
        zoom_object = generate_object(config=config)
    COMMANDS = get_commands(zoom_object)

    while True:
        for command in SELECTION_QUEUE:
            if command in COMMANDS:
                pass
        SELECTION_QUEUE.clear()

        if not zoom_object.is_terminal_focused():
            zoom_object.open_terminal()
        
        SELECTION_QUEUE = input('>> ').strip().lower().split()

