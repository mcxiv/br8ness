# -*- coding: utf-8 -*-
# --------------------------------------------------
# br8ness - A simple brightness amplifier for certain focused windows
# Quentin 'MCXIV' Dufournet, 2023
# --------------------------------------------------
# Built-in
import os
import time
import sys

# 3rd party
import Xlib.display
import psutil

# --------------------------------------------------


def get_displays():
    """
    The function "get_displays" uses the xrandr command to list all connected monitors and returns a
    list of their names.
    :return: a list of the names of all connected displays.
    """

    output = os.popen('xrandr --listmonitors').read()
    output = output.split('\n')

    return [element.split(' ')[-1] for element in output[1:] if element != '']


def get_focused_window_info():
    """
    The function retrieves the name of the currently focused window's process using Xlib and psutil
    libraries in Python.
    :return: the name of the process that owns the currently focused window.
    """

    display = Xlib.display.Display()
    root_win = display.screen().root
    focused_win_id = root_win.get_full_property(display.intern_atom(
        '_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    focused_win = display.create_resource_object('window', focused_win_id)

    win_pid = focused_win.get_full_property(display.intern_atom(
        '_NET_WM_PID'), Xlib.X.AnyPropertyType).value[0]

    return psutil.Process(win_pid).name()


if __name__ == '__main__':
    # The list of processes that will trigger the brightness change
    list_of_process = os.getenv('BR8NESS_LIST_OF_PROCESS')
    if list_of_process == '' or list_of_process is None:
        sys.exit('The environment variable BR8NESS_LIST_OF_PROCESS is not set.')
    list_of_process = list_of_process.split(',')

    # Timer to avoid calling too many times the system command
    # that lists the connected displays
    timer_display = 0

    # The flag is used to avoid calling too many times the system command
    flag_brightness = False

    # The list of displays to change the brightness
    displays = get_displays()
    # Set the brightness to 1.0 at the beginning
    for display in displays:
        os.system(f'xrandr --output {display} --brightness 1.0')

    while 1:
        try:
            focus = get_focused_window_info()
        except Exception as e:
            focus = None
            print(e)

        if time.time() - timer_display > 5:
            # The list of displays to change the brightness
            displays = get_displays()
            timer_display = time.time()

        if focus in list_of_process and not flag_brightness:
            for display in displays:
                os.system(f'xrandr --output {display} --brightness 1.8')
            flag_brightness = True
        elif focus not in list_of_process and flag_brightness:
            for display in displays:
                os.system(f'xrandr --output {display} --brightness 1.0')
            flag_brightness = False

        # The sleep is used to avoid calling too many times the system command
        try:
            time.sleep(0.1)

        # Incase of having the script running in a terminal
        except KeyboardInterrupt:
            for display in displays:
                os.system(f'xrandr --output {display} --brightness 1.0')
            sys.exit(0)
