import os
import PySimpleGUI as sg
from pathlib import Path
import json

#podriamos dividir esto en más programas más específicos

# ROUTES
def_windows_dir = os.path.dirname(os.path.realpath(__file__))
images_dir = os.path.join(Path(def_windows_dir).parent.parent.parent,"data","images")
profiles_dir = os.path.join(Path(def_windows_dir).parent.parent,"data","users")

long_button_dir = os.path.join(images_dir,"LongButton.png")
back_button_dir = os.path.join(images_dir,"buttonback.png")
x_button_dir = os.path.join(images_dir,"buttonx.png")
background_dir = os.path.join(images_dir,"Landscape5_2.png")
background_dir_2 = os.path.join(images_dir,"Landscape5_1.png")
avatar_button_dir = os.path.join(images_dir,"prueba_avatar_button.png")

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

# MISCELÁNEOS
font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)


# MENU WINDOW
menu_events = ["-PLAY-","-SETTINGS-","-PROFILE-","-SCOREBOARD-"]
menu_layout = [
    #[sg.Titlebar(title = 'Figurace G14',text_color = "black",background_color = "LightBlue")],
    #[sg.Button(button_color=colors, image_filename=x_button_dir, border_width=1, key="-EXIT-", pad=(0,0))],
    [sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
    [sg.Button('PLAY', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PLAY-", pad=(115,0))],
    [sg.Button('SETTINGS', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SETTINGS-", pad=(115,0))],
    [sg.Button('PROFILE', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PROFILE-", pad=(115,0))],
    [sg.Button('SCOREBOARD', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SCOREBOARD-", pad=(115,0))],
    [sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
]
menu_window = sg.Window('Figurace G14', menu_layout, margins=(0,0))


# PROFILE WINDOW
profile_events = ["-LOAD-","-NEW-","-DELETE-","-BACK-"]
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
profile_window = sg.Window('Figurace G14 - Profile', profile_buttons_layout, margins=(0,0))


# NEW PROFILE WINDOW
new_profile_events = ["-AVATAR-","-SAVE-"]
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
new_profile_window = sg.Window('Figurace G14 - New Profile', new_profile_layout, margins=(0,0))


# CHOOSE AVATAR
avatar_events = ["-SAVE-","-AVATAR1-","-AVATAR2-","-AVATAR3-","-AVATAR4-","-AVATAR5-","-AVATAR6-","-AVATAR7-","-AVATAR8-","-AVATAR9-"]

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

avatars_window = sg.Window("Figurace G14 - Avatar Selection", avatars_layout, margins=(0,0))