"""
dado el archivo denominado BBB_nuevo.csv que contiene los accesos al recurso
BigBlueButton que usamos para las clases virtuales de la materia,
se desea generar una archivo con todos aquellos usuarios que visualizaron la grabación el día 6 de abril.
"""

import csv
import os

dir = os.path.realpath(".")
dir_BBB = os.path.join(dir,"BBB_nuevo.csv")
dir_present = os.path.join(dir,"presentes_abril_6.csv")

with open(dir_BBB,"r",encoding="utf8") as bbb_file:
    bbb_reader = csv.reader(bbb_file, delimiter=",")
    header = next(bbb_reader)
    with open(dir_present,"w",encoding="utf8",newline="") as present_file:
        present_writer = csv.writer(present_file)
        present_writer.writerows(map(lambda y: [y[1]], filter(lambda x: ("6/04/2022" in x[0]) and (x[2] == "Grabación vista"),bbb_reader)))
