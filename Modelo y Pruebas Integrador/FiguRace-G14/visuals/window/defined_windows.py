import os
import PySimpleGUI as sg
from pathlib import Path
import json

#podriamos dividir esto en más programas más específicos

# ROUTES
def_windows_dir = os.path.dirname(os.path.realpath(__file__))
images_dir = os.path.join(Path(def_windows_dir).parent.parent,"data","images")
profiles_dir = os.path.join(Path(def_windows_dir).parent.parent,"data","users")

long_button_dir = os.path.join(images_dir,"LongButton.png")
back_button_dir = os.path.join(images_dir,"buttonback.png")
x_button_dir = os.path.join(images_dir,"buttonx.png")
background_dir = os.path.join(images_dir,"Landscape5_2.png")
background_dir_2 = os.path.join(images_dir,"Landscape5_1.png")
avatar_button_dir = os.path.join(images_dir,"prueba_avatar_button.png")


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
    [sg.Button(button_color=colors, font=font, image_filename=avatar_button_dir, border_width=0, key="-AVATAR-", pad=(10,20))]
]
new_profile_layout = [
    [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(20,10))],
    #[sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
    [sg.Column(new_profile_avatar_column), sg.Column(new_profile_text_column), sg.Column(new_profile_input_column, vertical_alignment='center', justification='center',  k='-C-')],
    [sg.Button('SAVE', button_color=colors, font=font, image_filename=long_button_dir, border_width=0, key="-SAVE-", pad=(115,50))]
    #[sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
]
new_profile_window = sg.Window('Figurace G14 - New Profile', new_profile_layout, margins=(0,0))

