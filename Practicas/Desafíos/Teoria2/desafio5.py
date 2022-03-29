def cargar_alumnos(end_name: str):
    lista_notas = []
    aux_nombre = input("Ingrese un nombre: ")
    while(aux_nombre != end_name):
        aux_nota = float(input(f"Ingrese la nota de {aux_nombre}: "))
        lista_notas.append((aux_nombre,aux_nota))
        aux_nombre = input("Ingrese un nombre: ")
    return lista_notas

def calcular_promedio(lista_notas):
    total = 0
    for aux_alumno in lista_notas:
        total = total + aux_alumno[1]
    promedio = total / len(lista_notas)
    return promedio

def imprimir_bajo_promedio(lista_notas, promedio: float):
    for aux_alumno in lista_notas:
        if(aux_alumno[1] < promedio):
            print(f"{aux_alumno[0]} se encuentra bajo el promedio, con una nota de {aux_alumno[1]}")
    
lista_notas = cargar_alumnos("FIN")
if(lista_notas != []):
    print("----------- Alumnos ingresados -------------")
    promedio = calcular_promedio(lista_notas)
    print(f"El promedio de las notas es: {promedio}")
    print("\n Alumnos bajo el promedio: ")
    imprimir_bajo_promedio(lista_notas,promedio)
else:
    print("No se ingresaron alumnos!")
