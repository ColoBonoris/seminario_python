lista_notas = []
aux_alumno = [input("Ingrese un nombre: "),float(input("Ingrese la nota: "))]
while(aux_alumno[0] != "FIN"):
    lista_notas.append(aux_alumno)
    aux_alumno = [input("Ingrese un nombre: "),float(input("Ingrese la nota: "))]
if(lista_notas != []):
    print("----------- Alumnos ingresados -------------")
    total = 0
    for aux_alumno in lista_notas:
        total = total + aux_alumno[1]
    promedio = total / len(lista_notas)
    print(f"El promedio de las notas es: {promedio}")
    print("\n Alumnos bajo el promedio: ")
    for aux_alumno in lista_notas:
        if(aux_alumno[1] < promedio):
            print(f"{aux_alumno[0]} se encuentra bajo el promedio, con una nota de {aux_alumno[1]}")
else:
    print("No se ingresaron alumnos!")
