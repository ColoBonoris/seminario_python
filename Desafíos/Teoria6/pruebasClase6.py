import PySimpleGUI as sg
layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
    [sg.Text('Ingresá segundo valor'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window("Segunda Demo", layout, margins=(200, 150))
while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
print('Datos ingresados: ', values)
window.close()