import os
import PySimpleGUI as sg
from visuals.window.defined_windows import *
from choose_avatar import new_avatar

#efined_windows_dir = os.path.join("visuals","window","defined_windows.py")

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
        "avatar": new_avatar_dir,
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
