import os
import PySimpleGUI as sg
from visuals.window.defined_windows import *
from open_profile import open_profile

defined_windows_dir = os.path.join("visuals","window","defined_windows.py")

def menu():
    while True:
        event, values = menu_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event in menu_events:
            menu_window.close()
            match event:
                case "-PLAY-":
                    try:
                        play_figurace()
                    except:
                        print("Pantalla de juego aún no construída.")
                case "-SETTINGS-":
                    try:
                        open_settings()
                    except:
                        print("Pantalla de configuración aún no construída.")
                case "-PROFILE-":
                    try:
                        open_profile()
                    except:
                        print("Pantalla de perfil aún no construída.")
                case "-SCOREBOARD-":
                    try:
                        show_scoreboard()
                    except:
                        print("Pantalla de puntajes aún no construída.")
                        
    menu_window.close()

menu()