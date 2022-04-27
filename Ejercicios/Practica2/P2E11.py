"""

Con la información de los archivos de texto que se encuentran disponibles en el curso:

    nombres_1
    nombres_2

•   Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
•   Genere tres variables con la lista de notas y nombres que se incluyen en los archivos:
    nombres_1, eval1.txt y eval2.txt e imprima con formato los nombres de los estudiantes 
    con las correspondientes nota y la suma de ambas como se ve en la imagen

"""
# Apertura de archivos
nombres_1 = open("nombres_1.txt","r",encoding="utf8")
nombres_2 = open("nombres_2.txt","r",encoding="utf8")
notas_0 = open("eval1.txt","r",encoding="utf8")
notas_1 = open("eval2.txt","r",encoding="utf8")
# Lectura de archivos
nombres_1 = nombres_1.read().replace("'","").replace(" ","").replace("\n","").split(",")
nombres_2 = nombres_2.read().replace("'","").replace(" ","").replace("\n","").split(",")
notas_0 = notas_0.read().replace("'","").replace(" ","").replace("\n","").split(",")
notas_1 = notas_1.read().replace("'","").replace(" ","").replace("\n","").split(",")
# Conseguimos los nombres repetidos para el primer punto y los imprimimos
nombres_repetidos = set([i.lower() for i in nombres_1 if i in nombres_2])
print("\n------------|  Nombres Repetidos:\n")
print(nombres_repetidos)
# Imprimimos los datos que se piden con el formato especificado
print("\n--------------------------------------------------------------------------------------------------------------------\n")
encabezado = ["","Nombre","Eval 1","Eval 2","Total"]
print(f"{encabezado[0]:<5}{encabezado[1]:<20}{encabezado[2]:^20}{encabezado[3]:^30}{encabezado[4]:^40}")
for i in range(len(nombres_1)):
    total = int(notas_0[i]) + int(notas_1[i])
    print(f"{(i+1):<5}{nombres_1[i]:<20}{notas_0[i]:^20}{notas_1[i]:^30}{total:^40}")
print("\n--------------------------------------------------------------------------------------------------------------------\n")