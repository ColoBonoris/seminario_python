import os
import PySimpleGUI as sg

defined_windows_dir = os.path.join("visuals","window","defined_windows.py")
import def_windows


def menu():
    while True:
        try:
            event, values = menu_window.read()
        except:
            print("Pantalla de menú aún no construída.")
            break
        if event == sg.WINDOW_CLOSED:
            break
        elif event in defined_windows:
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