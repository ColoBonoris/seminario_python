# Solución alternativa
from collections import Counter
import csv
import os #

def usuarios_mayor_interaccion(dir_csv):
    # Me parece correcta y eficiente la forma en la que determina los 3 con más apariciones, solo cambio el open por un with open() y elimino close()
    """
        Recibe la dirección de un archivo csv y devuelve una lista con lo pedido en la consigna .
    """
    with open (dir_csv, 'r') as archivo: #
        delimitado = csv.reader(archivo, delimiter = ',')
        usuarios = map(lambda fila:fila[1] , delimitado)
        tres_usuarios_mas_activos = Counter(usuarios).most_common(3)
    print(type(tres_usuarios_mas_activos[0]))
    return tres_usuarios_mas_activos

# Agrego el uso de os.path, si hay cambios en la direccion de destino del archivo es más fácil de modificar, y más adecuado
dir = os.path.realpath(".") #
dir_csv = os.path.join(dir,"TOTAL_nuevo.csv") #

# La forma en la que imprime cumple y me parece correcta
print ('Los 3 usuarios con mas actividad son:')
for i in usuarios_mayor_interaccion(dir_csv):
    print (f'{i[0]} con {i[1]} participaciones' )
