import os
import PySimpleGUI as sg
import json
from visuals.window.directions import *
from choose_avatar import new_avatar

#efined_windows_dir = os.path.join("visuals","window","defined_windows.py")

new_profile_events = ["-AVATAR-","-SAVE-"]

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

def create_profile_window():
    new_profile_input_column = [
        [sg.InputText(pad=(10,10))],
        [sg.InputText(pad=(10,10))]
    ]
    new_profile_text_column = [
        [sg.Text('Name',font=font,text_color="black",background_color="LightBlue",pad=(0,10))],
        [sg.Text('Nick',font=font,text_color="black",background_color="LightBlue",pad=(0,10))]
    ]
    new_profile_avatar_column = [
        [sg.Button(button_color=colors, font=font, image_filename=avatars_dir[0], border_width=0, key="-AVATAR-", pad=(10,20))]
    ]
    new_profile_layout = [
        [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(20,10))],
        #[sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
        [sg.Column(new_profile_avatar_column), sg.Column(new_profile_text_column), sg.Column(new_profile_input_column, vertical_alignment='center', justification='center',  k='-C-')],
        [sg.Button('SAVE', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-SAVE-", pad=(115,50))]
        #[sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
    ]
    return sg.Window('Figurace G14 - New Profile', new_profile_layout, margins=(0,0))

def create_new_player(values, avatar_number):
    """
        Creates a new player, receiving name (values[0]) and nick (values[1]).
        Further profile values get initialized on 0
    """
    new_profile_dir = os.path.join(profiles_dir,(values[1] + ".json"))
    new_avatar_dir = os.path.join(avatar_dir,(f"avatar{avatar_number}.jpg"))
    #if not os.path.exists(new_profile_dir):
    new_player = {
        # falta agregar la lopción de avatar
        "name": values[0],
        "nick": values[1],
        "avatar": avatars_dir[avatar_number],
        "played": 0,
        "top_1": 0,
        "top_2": 0,
        "top_3": 0
    }
    with open(new_profile_dir,"w",encoding="utf-8",newline="") as new_profile_file:
        #Acá faltaría hacer bien la conversión de caracteres para prevención de errores
        json.dump(new_player,new_profile_file)
    actual_player_dir = new_profile_dir

def new_profile():
    avatar_number = 0
    new_profile_window = create_profile_window()
    while True:
        event, values = new_profile_window.read()
        if event == "-BACK-" or event == sg.WINDOW_CLOSED or event == "-SAVE-":
            if event == "-SAVE-":
                create_new_player(values,avatar_number)
            break
        elif event == "-AVATAR-":
            new_profile_window.Hide()
            avatar_number = new_avatar()
            new_profile_window.UnHide()
    new_profile_window.close()
