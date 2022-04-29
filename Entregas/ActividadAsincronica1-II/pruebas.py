"""
    Solución alternativa.
    Mejora un poco el manejo del archivo y llega al mismo resultado de una forma diferente.
    En las bases, de todas formas, es un tratamiento parecido de los datos, el cual seria bastante más
    "limpio" utilizando las funciones de Counter.
"""

import csv
import os #

# Agrego el uso de os.path, si hay cambios en la direccion de destino del archivo es más fácil de modificar, y más adecuado
dir = os.path.dirname(__file__) #
dir_csv = os.path.join(dir,"TOTAL_nuevo.csv") #
# Se hace el tratamiento de la imformación
with open (dir_csv, 'r') as archivo: #
        csv_file = csv.reader(archivo, delimiter = ',')
        header = next(csv_file)
        # Obtenemos una lista con los nombres
        usuarios = list(map(lambda fila: fila[1], csv_file))
        # Se genera un diccionario nombre: apariciones
        apariciones = {}
        for i in set(usuarios):
            apariciones[i] = 0
        # Se calculan las apariciones de cada nombre
        for i in usuarios:
            apariciones[i] += 1
        # Obtenemos los 3 maximos
        maximos_actividad = []
        copia_apariciones = apariciones.copy()
        for i in range(3):
            maximo = max(copia_apariciones, key=copia_apariciones.get)
            maximos_actividad.append((maximo,copia_apariciones[maximo]))
            del copia_apariciones[maximo]
# Imprimimos los 3 valores obtenidos
for i in maximos_actividad:
    print (f'{i[0]}: {i[1]} participaciones totales.' )
