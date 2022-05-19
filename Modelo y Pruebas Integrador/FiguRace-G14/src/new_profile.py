import os
import PySimpleGUI as sg

defined_windows_dir = os.path.join("visuals","window","defined_windows.py")
import defined_windows

def create_new_player(values):
    """
        Creates a new player, receiving name (values[0]) and nick (values[1]).
        Further profile values get initialized on 0
    """
    new_profile_dir = os.path.join(profiles_dir,(values[1] + ".json"))
    #if not os.path.exists(new_profile_dir):
    new_player = {
        "name": values[0],
        "nick": values[1],
        "played": 0,
        "top_1": 0,
        "top_2": 0,
        "top_3": 0
    }
    with open(new_profile_dir,"w",encoding="utf-8",newline="") as new_profile_file:
        #Acá faltaría hacer bien la conversión de caracteres para prevención de errores
        json.dump(new_player,new_profile_file)
    actual_player_dir = new_profile_dir

while True:
    event, values = new_profile_window.read()
    if event == "-BACK-" or event == sg.WINDOW_CLOSED or event == "-SAVE-":
        if event == "-SAVE-":
            create_new_player(values)
        break
new_profile_window.close()






