import os
import PySimpleGUI as sg

background_dir = os.path.join("data","images","Landscape5_2.png")
background_dir_2 = os.path.join("data","images","Landscape5_1.png")
button_dir = os.path.join("data","images","button1.png")
long_button_dir = os.path.join("data","images","LongButton.png")
font = ('Arial 12 bold')
sg.theme('Dark')
sg.set_options(font=font)
colors = (sg.theme_background_color("black"), sg.theme_background_color("DarkOrange3"))

#falta ajustar posición y tamaños

buttons_layout = [
    [sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
    [sg.Button('PLAY', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PLAY-", pad=(115,0))],
    [sg.Button('SETTINGS', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SETTINGS-", pad=(115,0))],
    [sg.Button('PROFILE', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PROFILE-", pad=(115,0))],
    [sg.Button('SCORES', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SCORES-", pad=(115,0))],
    [sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
]

background_layout = [
    [sg.Image(background_dir)]
]

#window_buttons = sg.Window('Figurace G14', buttons_layout, margins=(0,0), finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)
#window_background = sg.Window('Background', background_layout, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[[''], ['Exit',]])
#window_background.bring_to_front()
#window_buttons.bring_to_front()
#window_buttons.TKroot.transient(window_background.TKroot)
#window_buttons.TKroot.grab_set()

window_buttons = sg.Window('Figurace G14', buttons_layout, margins=(0,0))


while True:
    #event, values = window_background.read()
    event, values = window_buttons.read()
    if event == sg.WINDOW_CLOSED:
        break
window_buttons.close()
#window_background.close()