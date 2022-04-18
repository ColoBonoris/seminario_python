"""
• Dado el conjunto de datos con series y películas de Netflix, queremos:
1- guardar en otro archivo las peliculas agregadas en el año 2021.
2- los cinco (5) países con más producciones en Netflix.
"""
from collections import Counter
import os
import csv

ruta = os.path.dirname(os.path.realpath("."))
ruta = os.path.join(ruta,"SI207 Seminario de Lenguajes (Python)", "Practicas", "Desafíos", "Teoria4")
ruta_netflix = os.path.join(ruta, "Datos", "netflix_titles.csv")
ruta_2021 = os.path.join(ruta, "Datos", "2021_titles.csv")

with open(ruta_netflix,"r",encoding="utf8") as titulos:
    titulos_csv = csv.reader(titulos,delimiter=",")
    encabezado =  next(titulos_csv)
    paises = list(filter(lambda x: x != "",map(lambda x: x[5],titulos_csv)))

with open(ruta_netflix,"r",encoding="utf8") as titulos:
    titulos_csv = csv.reader(titulos,delimiter=",")
    encabezado =  next(titulos_csv)
    with open(ruta_2021,"w",encoding="utf8") as titulos_2021:
        titulos_2021 = csv.writer(titulos_2021)
        titulos_2021.writerow(encabezado)
        titulos_2021.writerows(filter(lambda x: x[7] == "2021",titulos_csv))

paises = Counter(paises)
top_paises = paises.most_common(5)
print(top_paises)
# seek 0 en el csv, agregar un counter y contar la cantidad de países

