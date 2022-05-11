import os
import PySimpleGUI as sg

background_dir = os.path.join("data","images","landscape1.png")
button_dir = os.path.join("data","images","button1.png")
font = ('Arial', 9, 'bold')
sg.theme('Dark')
sg.set_options(font=font)
colors = (sg.theme_background_color('black'), sg.theme_background_color('teal'))

#falta ajustar posición y tamaños

buttons_layout = [
    [sg.Button('PLAY', button_color=colors, image_filename=button_dir, border_width=0, key="-PLAY-", pad=(0, 0), size=(100, 100))],
    [sg.Button('SETTINGS', button_color=colors, image_filename=button_dir, border_width=0, key="-SETTINGS-", pad=(0, 0))],
    [sg.Button('PROFILE', button_color=colors, image_filename=button_dir, border_width=0, key="-PROFILE-", pad=(0, 0))],
    [sg.Button('SCORES', button_color=colors, image_filename=button_dir, border_width=0, key="-SCORES-", pad=(0, 0))]
]

background_layout = [
    [sg.Image(background_dir, pad=(0,0), size=(300,300))]
]

window_buttons = sg.Window('Figurace G14', buttons_layout, margins=(500,400))

window_background = sg.Window('FiguRace G14', background_layout, margins=(500,400))

while True:
    event, values = window_background.read()
    #event, values = window_buttons.read()
    if event == sg.WINDOW_CLOSED:
        break
#window_buttons.close()
window_background.close()