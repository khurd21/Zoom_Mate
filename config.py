
import os
from dataclasses import dataclass

basedir = os.path.abspath(os.path.dirname(__file__))


@dataclass
class Config:
    ROOT_PATH    :str = basedir
    IMG_PATH     :str = os.path.join(ROOT_PATH, 'files/imgs')
    MEETINGS_CSV :str = os.path.join(ROOT_PATH, 'files/.meetings.csv')

    WAIT_TIME_BETWEEN_COMMANDS = 0.5