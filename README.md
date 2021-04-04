# Zoom Mate

Are you tired of using the Zoom GUI to join calls, toggle your video and audio, or to share you screen? You should try Zoom Mate, a terminal-based program to control Zoom.

# How Does Zoom Mate Work?

Type in 'join' to receive a list of your scheduled meetings. To select which meeting to join, simply type the number alongside each meeting. You are welcome to add or remove meetings in the settings.json file [make sure the syntax is correct!].

Once you have selected the meeting to join, Zoom will begin to launch, adding you to the call and connecting you to computer audio, all without intervention! Once in a call, you can use any of the commands that are described below.

You can also list multiple commands in a queue-like fashion that will execute in order. For example:

'unmute display share' will first unmute your audio, turn on video, and share your screen.
'join <id_num> mute undisplay' will join the zoom meeting of a specified id and make sure your audio and video is off.

# Commands to Get Started

open      - launches the zoom.us application

join      - presents a list of zoom meetings to join

# Commands Once in a Call

display   - turns on your video

undisplay - turns off your video

mute	  - mutes your audio

unmute    - unmutes your audio

share     - shares you primary screen

unshare   - stops sharing of your screen

leave     - leaves the meeting

exit	  - quits zoom and ends the program

# Requirements

- Python3.7 on MacOS (11.0.1)

- Virtual Environment (pip3 install virtualenv)

- Install dependencies using 'make install'

- Run program using 'make run'

# Remarks

- The program is only working for MacOS, tested on version 11.0.1. I intend to work on getting support for Windows and Linux devices.

- Program has only been tested on an iMac with 4k resolution and a MacBook Pro with 2k resolution.

- If your computer is slow, you can adjust the speed in which the commands will execute within the globals.py file [WAIT_TIME_BETWEEN_COMMANDS = <float_val>
