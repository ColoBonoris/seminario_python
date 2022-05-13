# deberian importarse capaz módulos del programa
import os
import PySimpleGUI as sg

# ESto debería hacerse más ordenado y usando try/except
background_dir = os.path.join("data","images","Landscape5_2.png")
background_dir_2 = os.path.join("data","images","Landscape5_1.png")
button_dir = os.path.join("data","images","button1.png")
x_button_dir = os.path.join("data","images","buttonx.png")
long_button_dir = os.path.join("data","images","LongButton.png")

font = ('Arial 12 bold')
sg.theme('Dark')
sg.set_options(font=font)
colors = (sg.theme_background_color("black"), sg.theme_background_color("DarkOrange3"))

defined_windows = ["-PLAY-","-SETTINGS-","-PROFILE-","-SCORES-"]
buttons_layout = [
    [sg.Button(button_color=colors, image_filename=x_button_dir, border_width=1, key="-EXIT-", pad=(0,0))],
    [sg.Image(background_dir,background_color = sg.theme_background_color(),pad=(0,0))],
    [sg.Button('PLAY', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PLAY-", pad=(115,0))],
    [sg.Button('SETTINGS', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SETTINGS-", pad=(115,0))],
    [sg.Button('PROFILE', button_color=colors, image_filename=long_button_dir, border_width=0, key="-PROFILE-", pad=(115,0))],
    [sg.Button('SCOREBOARD', button_color=colors, image_filename=long_button_dir, border_width=0, key="-SCOREBOARD-", pad=(115,0))],
    [sg.Image(background_dir_2,background_color = sg.theme_background_color(),pad=(0,0))]
]

window_buttons = sg.Window('Figurace G14', buttons_layout, margins=(0,0))

while True:
    event, values = window_buttons.read()
    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break
    elif event in defined_windows:
        window_buttons.close()
        match event:
            case "-PLAY-":
                play_figurace()
            case "-SETTINGS-":
                open_settings()
            case "-PROFILE-":
                open_profile()
            case "-SCOREBOARD-":
                show_scoreboard()

window_buttons.close()
