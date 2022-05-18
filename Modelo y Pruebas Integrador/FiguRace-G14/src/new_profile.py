import os
import PySimpleGUI as sg

defined_windows_dir = os.path.join("visuals","window","defined_windows.py")
import def_windows

while True:
    event, values = window_new_profile.read()
    if event == "-BACK-" or event == sg.WINDOW_CLOSED or event == "-SAVE-":
        if event == "-SAVE-":
            new_profile_dir = os.path.join(profiles_dir,(values[2] + ".json"))
            #if not os.path.exists(new_profile_dir):
            new_player = {
                "name": values[1],
                "nick": values[2],
                "played": 0,
                "top_1": 0,
                "top_2": 0,
                "top_3": 0
            }
            with open(new_profile_dir,"w",encoding="utf-8",newline="") as new_profile_file:
               json.dump(new_player,new_profile_file)
            actual_player_dir = new_profile_dir
        break
window_new_profile.close()






