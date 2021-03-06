import os
import PySimpleGUI as sg
import json
from src.directions import *
from src.choose_avatar import new_avatar

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

def create_new_player(name, nick, avatar_number):
    """
        Creates a new player, receiving name, nick and avatar number.
        Further profile values get initialized on 0
    """
    new_profile_dir = os.path.join(users_dir,(nick + ".json"))
    new_avatar_dir = os.path.join(avatar_dir,(f"avatar{avatar_number}.jpg"))
    #if not os.path.exists(new_profile_dir):
    new_player = {
        # falta agregar la lopci??n de avatar
        "name": name,
        "nick": nick,
        "avatar": avatar_number,
        "played": 0,
        "top_1": 0,
        "top_2": 0,
        "top_3": 0
    }
    if(os.path.exists(users_dir)):
        with open(users_dir,"r",encoding="utf-8",newline="") as users_file:
            #Ac?? faltar??a hacer bien la conversi??n de caracteres y prevenci??n de errores
            players_list = json.load(users_file)
            players_list.append(new_player)
            new_player = players_list
    else:
        new_player = [new_player]
    with open(users_dir,"w",encoding="utf-8",newline="") as users_file:
        #Ac?? faltar??a hacer bien la conversi??n de caracteres y prevenci??n de errores
        json.dump(new_player,users_file)

def new_profile():
    avatar_number = 0
    new_profile_window = create_profile_window()
    while True:
        event, values = new_profile_window.read()
        if event == "-BACK-" or event == sg.WINDOW_CLOSED or event == "-SAVE-":
            if event == "-SAVE-":
                create_new_player(values[0], values[1], avatar_number)
                new_profile_window.close()
            break
        elif event == "-AVATAR-":
            new_profile_window.Hide()
            avatar_number = new_avatar()
            new_profile_window.UnHide()
    
