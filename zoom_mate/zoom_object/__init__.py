import platform
from config import Config


_OBJECT = None
_SYSTEM = platform.system()

if _SYSTEM == 'Darwin':
    from ._mac_os import _MAC_OS
    _OBJECT = _MAC_OS
elif _SYSTEM == 'Linux':
    raise NotImplementedError(f'{_SYSTEM} is not supported yet.')
elif _SYSTEM == 'Windows':
    raise NotImplementedError(f'{_SYSTEM} is not supported yet.')



def generate_object(config=Config):
    if _OBJECT:
        return _OBJECT(config=config)
    raise Exception(f'Operating System {_SYSTEM} not supported.')