"""
Reemplazar el valor de “Position” (pos 3 en csv) por las posiciones en español. Por ejemplo “LB|CB”
debe ser reemplazado por “Defensor izquierdo|Defensor central
"""

import csv
import os
import json
"""
dic = {
"CF":"Media Punta",
"LW":"Extremo Izquierdo",
"RW":"Extremo Derecho",
"CAM":"Medio Centro Ofensivo",
"LM":"Medio Izquierdo",
"CM":"Medio Central",
"RM":"Medio Derecho",
"CDM":"Medio Centro Defensivo",
"LWB":"Carrilero Izquierdo",
"RWB":"Carrilero Derecho",
"LB":"Defensor Izquierdo",
"CB":"Defensor Centro",
"RB":"Defensor Derecho",
"GK":"Arquero"
}
"""
def filter_positions(pos,dic_posiciones):
    positions = pos.split("|")
    pos = ""
    for i in range(len(positions)):
        positions[i] = dic_posiciones[positions[i]]
        pos += positions[i] + "|"
    pos = pos[0:len(pos)-1]
    return pos

this_route = os.path.dirname(__file__)
FIFA_route = os.path.join(this_route,"FIFA-21 Complete.csv")
new_FIFA_route = os.path.join(this_route,"new_FIFA-21 Complete.csv")
pos_route = os.path.join(this_route,"posiciones.txt")

print(FIFA_route)

with open(FIFA_route,"r",encoding="utf-8") as FIFA_file:
    FIFA_csv = csv.reader(FIFA_file,delimiter=";")
    header = next(FIFA_csv)
    lista_posiciones = list(map(lambda x: x[3], FIFA_csv))
    with open(pos_route,"r",encoding="utf-8")as posiciones:
        dic_posiciones = json.load(posiciones)
        for i in range(len(lista_posiciones)):
            lista_posiciones[i] = filter_positions(lista_posiciones[i],dic_posiciones)

with open(new_FIFA_route,"w",encoding="utf-8",newline="") as new_FIFA_file:
    with open(FIFA_route,"r",encoding="utf-8") as FIFA_file:
        FIFA_csv = csv.reader(FIFA_file,delimiter=";")
        new_FIFA_csv = csv.writer(new_FIFA_file,delimiter=";")
        header = next(FIFA_csv)
        new_FIFA_csv.writerow(header)
        rows = list(map(lambda x: x, FIFA_csv))
        for i in range(len(rows)):
            new_row = []
            for j in range(0,3):
                new_row.append(rows[i][j])
            new_row.append(lista_posiciones[i])
            for j in range(4,len(header)):
                new_row.append(rows[i][j])
            rows[i] = new_row[:]
        for i in rows:
            new_FIFA_csv.writerow(i)

