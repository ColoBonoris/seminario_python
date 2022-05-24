import os
import PySimpleGUI as sg
from src.directions import *

avatar_events = ["-SAVE-","-AVATAR1-","-AVATAR2-","-AVATAR3-","-AVATAR4-","-AVATAR5-","-AVATAR6-","-AVATAR7-","-AVATAR8-","-AVATAR9-"]

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

def create_avatars_window():
    avatars_layout = [
        [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(20,10))],
        [sg.Text("", pad=(0,15),text_color="black",background_color="LightBlue")],
        [sg.Text("CHOOSE YOUR AVATAR:", font="Arial 19 bold",text_color="black",background_color="LightBlue",pad=(30,0))],
        [
            sg.Button('', button_color=colors, image_filename=avatars_dir[0], border_width=0, key=avatar_events[1], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[1], border_width=0, key=avatar_events[2], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[2], border_width=0, key=avatar_events[3], pad=(10,10))
        ],
        [
            sg.Button('', button_color=colors, image_filename=avatars_dir[3], border_width=0, key=avatar_events[4], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[4], border_width=0, key=avatar_events[5], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[5], border_width=0, key=avatar_events[6], pad=(10,10))
        ],
        [
            sg.Button('', button_color=colors, image_filename=avatars_dir[6], border_width=0, key=avatar_events[7], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[7], border_width=0, key=avatar_events[8], pad=(10,10)),
            sg.Button('', button_color=colors, image_filename=avatars_dir[8], border_width=0, key=avatar_events[9], pad=(10,10))
        ],
        [sg.Text("", pad=(0,5),text_color="black",background_color="LightBlue")]
    ]
    return sg.Window("Figurace G14 - Avatar Selection", avatars_layout, margins=(0,0))

def new_avatar():
    avatars_window = create_avatars_window()
    while True:
        event, values = avatars_window.read()
        if event == "-BACK-" or event == sg.WIN_CLOSED:
            avatar = 1
            break
        elif (event in avatar_events):
            avatar = int(event[-2])
            break
    avatars_window.close()
    return avatar

