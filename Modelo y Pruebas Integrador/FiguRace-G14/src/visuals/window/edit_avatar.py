import PySimpleGUI as sg
import os
from pathlib import Path

def_windows_dir = os.path.dirname(os.path.realpath(__file__))
avatar_dir = os.path.join(Path(def_windows_dir).parent.parent.parent,"data","images","avatars")
avatars_dir = [
    os.path.join(avatar_dir,"avatar1.png"),
    os.path.join(avatar_dir,"avatar2.png"),
    os.path.join(avatar_dir,"avatar3.png"),
    os.path.join(avatar_dir,"avatar4.png"),
    os.path.join(avatar_dir,"avatar5.png"),
    os.path.join(avatar_dir,"avatar6.png"),
    os.path.join(avatar_dir,"avatar7.png"),
    os.path.join(avatar_dir,"avatar8.png"),
    os.path.join(avatar_dir,"avatar9.png")
]
images_dir = os.path.join(Path(def_windows_dir).parent.parent.parent,"data","images")
back_button_dir = os.path.join(images_dir,"buttonback.png")
long_button_dir = os.path.join(images_dir,"LongButton.png")

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

avatar_events = ["-SAVE-","-AVATAR1-","-AVATAR12-","-AVATAR3-","-AVATAR4-","-AVATAR5-","-AVATAR6-","-AVATAR7-","-AVATAR8-","-AVATAR9-"]

avatar_buttons = [
    [
        sg.Button('', button_color=colors, image_filename=avatars_dir[0], border_width=2, key=avatar_events[1], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[1], border_width=0, key=avatar_events[2], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[2], border_width=0, key=avatar_events[3], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[3], border_width=0, key=avatar_events[4], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[4], border_width=0, key=avatar_events[5], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[5], border_width=0, key=avatar_events[6], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[6], border_width=0, key=avatar_events[7], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[7], border_width=0, key=avatar_events[8], pad=(10,10)),
        sg.Button('', button_color=colors, image_filename=avatars_dir[8], border_width=0, key=avatar_events[9], pad=(10,10))
    ]
]

avatars_layout = [
    [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(20,10))],
    [sg.Text("", pad=(0,15),text_color="black",background_color="LightBlue")],
    [sg.Text("CHOOSE YOUR AVATAR:", font="Arial 19 bold",text_color="black",background_color="LightBlue")],
    [avatar_buttons[0:3]],
    [avatar_buttons[3:7]],
    [avatar_buttons[7:]],
    [sg.Text("", pad=(0,15),text_color="black",background_color="LightBlue")],
    [sg.Button('PICK', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-PICK-", pad=(115,50))],
    [sg.Text("", pad=(0,15),text_color="black",background_color="LightBlue")]
]

avatar_window = sg.Window("Figurace G14 - Avatar Selection", avatars_layout, margins=(0,0), element_justification='c')

while True:
    event, values = avatar_window.read()
    if event == sg.WINDOW_CLOSED:
        break

avatar_window.close()

