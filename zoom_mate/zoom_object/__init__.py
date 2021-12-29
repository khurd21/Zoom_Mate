import platform
from config import Config

from ._mac_os import _MAC_OS
from .base_object import ZoomObject


PLATFORMS = {
    'Darwin' : _MAC_OS,
    #'Linux'  : 'Not Implemented',
    #'Windows': 'Not Implemented',
}


def generate_object(config=Config):
    if (plt := platform.system()) in PLATFORMS.keys():
        return PLATFORMS[plt](config=config)
    raise Exception(f'Operating System {plt} not supported.')