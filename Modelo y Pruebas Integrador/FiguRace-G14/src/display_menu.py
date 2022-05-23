import os
import PySimpleGUI as sg
from visuals.window.directions import *
from open_profile import open_profile

menu_events = ["-PLAY-","-SETTINGS-","-PROFILE-","-SCOREBOARD-"]

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

def create_menu_window():
    menu_layout = [
        [sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
        [sg.Button('PLAY', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PLAY-", pad=(115,0))],
        [sg.Button('SETTINGS', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SETTINGS-", pad=(115,0))],
        [sg.Button('PROFILE', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PROFILE-", pad=(115,0))],
        [sg.Button('SCOREBOARD', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SCOREBOARD-", pad=(115,0))],
        [sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
    ]
    return sg.Window('Figurace G14', menu_layout, margins=(0,0))

def menu():
    menu_window = create_menu_window()
    while True:
        event, values = menu_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event in menu_events:
            menu_window.Hide()
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
            menu_window.UnHide()
    menu_window.close()

menu()