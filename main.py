#!/usr/bin/env python3

import platform

operating_system = platform.system()
if operating_system == 'Darwin':
    import _mac_os
    _mac_os.repl()


elif operating_system == 'Linux':
    pass


elif operating_system == 'Windows':
    pass