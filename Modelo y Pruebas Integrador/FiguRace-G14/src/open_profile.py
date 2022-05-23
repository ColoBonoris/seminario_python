import os
import PySimpleGUI as sg
from new_profile import create_new_player, new_profile
from visuals.window.directions import *

#defined_windows_dir = os.path.join("visuals","window","defined_windows.py")

profile_events = ["-LOAD-","-NEW-","-DELETE-","-BACK-"]

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

def create_profile_window():
    profile_buttons_column = [
        [sg.Button('LOAD PROFILE', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-LOAD-", pad=(115,0))],
        [sg.Button('NEW PROFILE', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-NEW-", pad=(115,10))],
        [sg.Button('DELETE PROFILE', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-DELETE-", pad=(115,0))]
    ]
    profile_buttons_layout = [
        [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(20,10))],
        [sg.Text("", pad=(0,10))],
        [sg.Column(profile_buttons_column, vertical_alignment='center', justification='center',  k='-C-')],
        [sg.Text("", pad=(0,15))]
    ]
    return sg.Window('Figurace G14 - Profile', profile_buttons_layout, margins=(0,0))

def open_profile():
    profile_window = create_profile_window()
    while True:
        event, values = profile_window.read()
        if event == sg.WINDOW_CLOSED or event == "-BACK-":
            break
        elif event in profile_events:
            profile_window.Hide()
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
            profile_window.UnHide()
    profile_window.close()
