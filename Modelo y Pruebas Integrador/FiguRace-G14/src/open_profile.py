import os
import PySimpleGUI as sg

defined_windows_dir = os.path.join("visuals","window","defined_windows.py")
import def_windows

while True:
    event, values = profile_window.read()
    if event == sg.WINDOW_CLOSED or event in profile_events:
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
