import os
import PySimpleGUI as sg
import json
from pathlib import Path
from src.display_menu import menu
from src.directions import *
from src.new_profile import create_new_player
#from data.users.loaded_users import current_users
# la idea sería que instancie un objeto jugador de
#Desde algún json (ultimo usado en ventana cache o sino el primero alfabético) y llame directo a las ventanas de src
# tiene que prevenir errores de falta de archivos

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(dir_path,"."))
#print(os.getcwd())

font = ('Arial 13 bold')
colors = (sg.theme_background_color("black"), sg.theme_background_color("LightBlue"))
sg.set_options(font=font)

def load_default_settings():
    if len(current_users) == 0:
        user = "default_user"
        if(os.path.join(users_dir,user) in os.listdir(users_dir)):
            create_new_player("User",user,1)
    else:
        user = current_users[0]
    default_settings = {
        "user": user,
        "music": True,
        "topic": "Mixed",
        "difficulty": "Medium"
        }
    with open(settings_dir,"w",encoding="utf-8",newline="") as default_settings_file:
        #Acá faltaría hacer bien la conversión de caracteres y prevención de errores
        json.dump(default_settings,default_settings_file)
    return default_settings

"""if(os.path.exists(settings_dir)):
    actual_settings = json.load(settings_dir)
else:
    actual_settings = load_default_settings()
print(actual_settings)"""
# Al final, sea lo que sea que haya pasado, actualiza el .json del jugador
# capaz para eso debería haber una carpeta bin o caché; que tendrá direcciones, el perfil en uso y los cambios (o algo así)
menu()