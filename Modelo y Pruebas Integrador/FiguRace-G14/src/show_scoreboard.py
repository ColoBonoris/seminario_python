import PySimpleGUI as sg
import json
from src.directions import *

colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
font0 = ("Arial 25 bold")
font = ('Arial 17 bold')
font2 = ("Arial 15 bold")
font3 = ("Arial 10")

def create_user_row(player_dict):
    """
        
    """
    avatar_column = [
        [sg.Image(os.path.join(avatar_dir,("avatar{}.png".format(player_dict["avatar"]))), background_color=colors[1])]
    ]
    avatar_nick_column = [
        [sg.Text(player_dict["name"], font=font, text_color=colors[0], background_color=colors[1])],
        [sg.Text(player_dict["nick"], font=font2, text_color=colors[0], background_color=colors[1])]
    ]
    scores_total = player_dict["top_1"] + player_dict["top_2"] + player_dict["top_3"]
    scores_column = [
        [sg.Text("#1: {}".format(player_dict["top_1"]), font=font3, text_color=colors[0], background_color=colors[1])],
        [sg.Text("#2: {}".format(player_dict["top_2"]), font=font3, text_color=colors[0], background_color=colors[1])],
        [sg.Text("#3: {}".format(player_dict["top_3"]), font=font3, text_color=colors[0], background_color=colors[1])],
        [sg.Text(f"Total: {scores_total}", font=font2, text_color=colors[0], background_color=colors[1])],
    ]
    return [sg.Column(avatar_column), sg.Column(avatar_nick_column, pad=(50,50)), sg.Column(scores_column)]
    #sg.Frame

def create_scoreboard_column():
    # podriamos usar una caja scrolleable
    """
        
    """
    with open(users_dir,"r",encoding="utf-8",newline="") as users_file:
        #Acá faltaría hacer bien la conversión de caracteres y prevención de errores
        players_list = json.load(users_file)
    if(len(players_list) > 0):
        scores_column = []
        for i in players_list:
            scores_column.append([sg.Frame("",[create_user_row(i)], background_color=colors[1], size=(540,170))])
        """scores_layout = [
            [sg.Frame(scores_layout)]
        ]"""
    else:
        pass #hacer algún cartelito, que no esté vació
    return sg.Column(scores_column,scrollable=True,vertical_scroll_only=True,size=(550,700))

def create_scoreboard_layout():
    return [
        [sg.Button(button_color=colors, image_filename=back_button_dir, border_width=0, key="-BACK-", pad=(0,0))],
        [sg.Text("SCORES",font=font0,text_color=colors[0],background_color=colors[1],pad=(200,10))],
        [sg.Text("",font=font0,text_color=colors[0],background_color=colors[1],pad=(0,0))],
        [sg.Frame("",[[create_scoreboard_column()]])]
    ]

def create_scores_window():
    #scoreboard_layout = create_scoreboard_layout()
    scoreboard_layout = create_scoreboard_layout()
    return sg.Window("Prueba scoreboards",scoreboard_layout,margins=(20,20),size=(600,800))

def show_scoreboard():
    scoreboard_window = create_scores_window()
    while True:
        event, values = scoreboard_window.read()
        if event == sg.WINDOW_CLOSED or event == "-BACK-":
            break
    scoreboard_window.close()
