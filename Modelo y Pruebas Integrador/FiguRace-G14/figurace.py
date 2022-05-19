import os

# la idea sería que instancie un objeto jugador desde algún json (ultimo usado en ventana cache o sino el primero alfabético) y llame directo a las ventanas de src
# tiene que prevenir errores de falta de archivos

class Player():
    # playersAmount = (cantidad de .json en carpeta users? Para tener una cuenta un poco más cierta? en var de clase)
    def __init__(self, player_dict):
        # Todos van a tener get, ninguno del
        # Tendrá sólo para aumentar en uno
        __amount_played = player_dict["played"]
        # Tendrán set, uso con cuidado
        __hi_score = player_dict["top_1"]
        __second_best = player_dict["top_2"]
        __third_best = player_dict["top_3"]
        # No se les puede hacer set
        __name = player_dict["name"]
        __nick = player_dict["nick"]
    def played_one(self):
        self.__amount_played += 1
    def eval_score(self,score):
        # ¿Habrá que usar setters también acá adentro?
        if(score > self.__third_best):
            if(score > self.__second_best):
                if(score > self.__hi_score):
                    self.__hi_score = score
                else:
                    self.__second_best = score
            else:
                self.__third_best = score
    # podríamos agregar una función de edición de perfil para cambiar avatar, nombre y/o nick




dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(dir_path,"."))
print(os.getcwd())

# Al final, sea lo que sea que haya pasado, actualiza el .json del jugador
# capaz para eso debería haber una carpeta bin o caché; que tendrá direcciones, el perfil en uso y los cambios (o algo así)
