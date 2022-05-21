import os
import PySimpleGUI as sg
from new_profile import create_new_player, new_profile
from visuals.window.defined_windows import *

#defined_windows_dir = os.path.join("visuals","window","defined_windows.py")

def open_profile():
    while True:
        event, values = profile_window.read()
        if event == sg.WINDOW_CLOSED or event in profile_events:
            profile_window.close()
            match event:
                case "-LOAD-":
                    try:
                        load_profile()
                    except:
                        print("Pantalla de carga de perfiles no encontrada")
                case "-NEW-":
                    try:
                        new_profile()
                    except:
                        print("Pantalla de creación de perfiles no encontrada")
                case "-DELETE-":
                    try:
                        delete_profile()
                    except:
                        print("Pantalla de eliminación de perfiles no encontrada")
            break
    profile_window.close()
