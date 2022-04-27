import string

def filtrar_lista_nombres(nombres):
    """
        Toma una lista de nombres y borra todos los caracteres
        que no sean letras. Mantiene mayúsculas y tildes.
    """
    for pos_nom in range(0,len(nombres)):
        for c in nombres[pos_nom]:
            if c not in (string.ascii_letters + ("ñáéíóúÑÁÉÍÓÚ")):
                nombres[pos_nom] = nombres[pos_nom].replace(c,"")
    return nombres

def filtrar_lista_notas(notas):
    """
        Toma una lista de notas y borra todos los caracteres
        que no sean numeros. Luego hace la conversión a int.
    """
    for pos_nota in range(0,len(notas)):
        for c in notas[pos_nota]:
            if c not in string.digits:
                notas[pos_nota] = notas[pos_nota].replace(c,"")
        notas[pos_nota] = int(notas[pos_nota])
    return notas

def imprimir_diccionario(dicc):
    """
        Imprime un diccionario (asumimos que es de alumnos por simplicidad)
    """
    print("\nAlumnos:\n")
    for i in dicc:
        print(f"    {i}, {dicc[i]}.")


# Abrimos los archivos
notas_0 = open("eval1.txt","r",encoding="utf8")
notas_1 = open("eval2.txt","r",encoding="utf8")
nombres = open("nombres_1.txt","r",encoding="utf8")
# Leemos los archivos
notas_0 = notas_0.read()
notas_1 = notas_1.read()
nombres = nombres.read()
# Separamos por alumno
notas_0 = notas_0.split("\n")
notas_1 = notas_1.split("\n")
nombres = nombres.split("\n")
# Filtramos los caracteres
notas_0 = filtrar_lista_notas(notas_0)
notas_1 = filtrar_lista_notas(notas_1)
nombres = filtrar_lista_nombres(nombres)
# Creamos una lista con las notas sumadas
merge_notas = []
for i in range(0,len(notas_0)):
    merge_notas.append(notas_0[i] + notas_1[i])
# Creamos el diccionario con alumno --> nota
dicc_alumnos = {}
for i in range(0,len(nombres)):
    dicc_alumnos[nombres[i]] = merge_notas[i]
imprimir_diccionario(dicc_alumnos)
# Sacamos el promedio
if(len(nombres) > 0):
    total_notas = 0
    for i in dicc_alumnos:
        total_notas += dicc_alumnos[i]
    promedio = total_notas / len(nombres)
else:
    print("No se pudo sacar el promedio, no se cargaron alumnos!")
print(f"\nPromedio: {promedio}.\n")
# Informamos los alumnos que no lo superan/igualan
print("\nAlumnos por debajo del promedio:\n")
for i in dicc_alumnos:
    if(dicc_alumnos[i] < promedio):
        print(f"    {i}, {dicc_alumnos[i]}.")
