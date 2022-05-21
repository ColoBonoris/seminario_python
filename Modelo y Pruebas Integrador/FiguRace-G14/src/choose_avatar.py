import os
import PySimpleGUI as sg
from visuals.window.defined_windows import *


def new_avatar():
    while True:
        event, values = avatars_window.read()
        if event == "-BACK-" or event == sg.WIN_CLOSED:
            avatar = 0
        elif (event in avatar_events):
            avatar = int(event[-2])
            break
    avatars_window.close()
    return avatar

