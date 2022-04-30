# Calcule cuántos dias pasaron entre el primer registro y el último

from asyncio.unix_events import DefaultEventLoopPolicy
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
    csv_BBB = list(csv_BBB)
    primer_dia = csv_BBB[0][0]
    ultimo_dia = csv_BBB[-1][0]
# Acá arrancan a haber errores
primer_dia_formato = datetime.datetime.strptime(primer_dia, formato_horario)
ultimo_dia_formato = datetime.datetime.strptime(ultimo_dia, formato_horario)
diferencia_dias_formato = str(ultimo_dia_formato - primer_dia_formato)
print(diferencia_dias_formato)
# print(f"""
#Diferencia horaria = :
#    Años: {diferencia_dias_formato.year()}
#    Meses: {diferencia_dias_formato.month()}
#    Horas: {diferencia_dias_formato.hour()}
#    Minutos: {diferencia_dias_formato.minute()}""")
