# Indique los días de la semana que más registros hubo

import os
import datetime
import csv
from collections import Counter

ruta = os.path.realpath(".")
ruta_datos = os.path.join(ruta,"Ejercicios","Practica3","BBB_nuevo.csv")

weekdays = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
formato_horario = "%d/%m/%Y %H:%M"

with open(ruta_datos,"r",encoding="utf8") as datos_BBB:
    csv_BBB = csv.reader(datos_BBB, delimiter = ",")
    header = next(csv_BBB)
    contador_dias = Counter(map(lambda x: datetime.datetime.strptime(x[0], formato_horario).weekday(), csv_BBB))
    weekday_amount = contador_dias.most_common()

for i in weekday_amount:
    print(f"{weekdays[i[0]]}: {i[1]} interacciones.")

