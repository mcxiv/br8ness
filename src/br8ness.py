# -*- coding: utf-8 -*-
# --------------------------------------------------
# br8ness - A simple brightness amplifier for certain focused windows
# Quentin 'MCXIV' Dufournet, 2023
# --------------------------------------------------
# Built-in
import os
import time

# 3rd party
import Xlib.display
import psutil

# --------------------------------------------------


list_of_process = ['x-terminal-emul', 'code-insiders']


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
    # The flag is used to avoid calling too many times the system command
    flag_brightness = False

    # Set the brightness to 1.0 at the beginning
    os.system('xrandr --output eDP-1 --brightness 1.0')

    while 1:
        focus = get_focused_window_info()
        if focus in list_of_process and not flag_brightness:
            os.system('xrandr --output eDP-1 --brightness 1.8')
            flag_brightness = True
        elif focus not in list_of_process and flag_brightness:
            os.system('xrandr --output eDP-1 --brightness 1.0')
            flag_brightness = False
        # The sleep is used to avoid calling too many times the system command
        time.sleep(0.1)
