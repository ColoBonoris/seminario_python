import PySimpleGUI as sg
import json
from src.directions import *

def create_user_row(player_dict):
    """
        
    """
    font = ('Arial 13 bold')
    font2 = "Arial 10 Bold"
    font3 = "Arial 8"
    avatar_column = [
        [sg.Image(os.path.join(avatar_dir,("avatar{}.png".format(player_dict["avatar"]))))]
    ]
    avatar_nick_column = [
        [sg.Text(player_dict["name"], font)],
        [sg.Text(player_dict["nick"], font2)]
    ]
    scores_total = player_dict["top_1"] + player_dict["top_2"] + player_dict["top_3"]
    scores_column = [
        [sg.Text(player_dict["top_1"], font3)],
        [sg.Text(player_dict["top_2"], font3)],
        [sg.Text(player_dict["top_3"], font3)],
        [sg.Text(f"Total: {scores_total}", font2)],
    ]
    return [sg.Column(avatar_column), sg.Column(avatar_nick_column), sg.Column(scores_column)]
    #sg.Frame

def create_scoreboard_layout():
    # podriamos usar una caja scrolleable
    """
        
    """
    with open(users_dir,"r",encoding="utf-8",newline="") as users_file:
        #Acá faltaría hacer bien la conversión de caracteres y prevención de errores
        players_list = json.load(users_file)
    if(len(players_list) > 0):
        scores_layout = []
        for i in players_list:
            scores_layout.append(create_user_row(i))
        """scores_layout = [
            [sg.Frame(scores_layout)]
        ]"""
    else:
        pass #hacer algún cartelito, que no esté vació

    return sg.Column(scores_layout,scrollable=True,vertical_scroll_only=True)
def create_scores_window():
    scoreboard_layout = create_scoreboard_layout()
    return sg.Window("Prueba scoreboards",scoreboard_layout,margins=(0,0))

def show_scoreboard():
    scoreboard_window = create_scores_window()
    while True:
        event, values = scoreboard_window.read()
        if event == sg.WINDOW_CLOSED:
            break
    scoreboard_window.close()
