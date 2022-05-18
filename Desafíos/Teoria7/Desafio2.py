"""
Dado el dataset con datos de video juegos del Apple store.
• Armar un menú con PySimpleGUi que permita:
1. listar los juegos gratuitos disponibles en idioma español.
2. los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count).
• Los que deseen, lo pueden subir a GitHub y compartir solución con @clauBanchoff
• Incluir manejo de excepciones donde consideren adecuado.
• También pueden descargar el archivo en: https://archivos.linti.unlp.edu.ar/index.php/s/D0YR0jqOx1GQtSDAyuda: para recuperar las imágenes de los íconos podemos usar el módulo requests - Se instala
con pip: pip install requests - +Info
"""

import PySimpleGUI as sg
import csv

sg.theme("Dark")
colors = (sg.theme_background_color("black"),sg.theme_background_color("green"))
font = ("Arial 12 bold")

main_layout = [
    #[sg.Title("EJERCICIO 1",font="comic sans 20 italics underlined bold",colors = (sg.theme_background_color("pink"),sg.theme_background_color("green")))],
    [sg.Button("LIST FREE GAMES IN SPANISH", button_color=colors, font=font, pad = (100,20), key="-LIST-", border_width=5)],
    [sg.Button("TOP USER RATING COUNT", button_color=colors, font=font, pad = (100,20), key="-TOP-", border_width=5)]
    ]
window = sg.Window("Desafio 2 Teoria 7", main_layout, margins = (0,0), size = (700,700))



# procesar csv

while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
        case "-LIST-":
            try:
                print(free_spanish_list)
            except NameError:
                print("EN CONSTRUCCIÓN...\nTodavía no tenemos los datos suficientes para responder eso")
        case "-TOP-":
            try:
                print(top_rating_list)
            except:
                print("EN CONSTRUCCIÓN...\nTodavía no tenemos los datos suficientes para responder eso")
window.close()



