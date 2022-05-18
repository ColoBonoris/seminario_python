"""
Ejecutá y analizá este código. Explicá qué hace. En caso de ser necesario modifícalo,
para que cuando se ingrese una burbuja que no existe saque el mensaje correcto
y, que continúe con el proceso.
"""

burbujas = {
    'A':("Pedro", "Ana","Roberto"),
    'B':("Juan","Rocio"),
    'C':("Ana","Roque","Celeste"),
    'D':("Juana","Renata"),
    'E':("Santiago","María", "Elena","Francisco"),
    'B':("Juan"),
    'F':("Pedro","Clara", "Anahi"),
    'G':("Sebastian","Reina", "Camilo")
}

def imprimir_integrantes(dicci):
    try:
        burbuja = input ('Ingresa nombre burbuja (A, B, C, D, E, F o G:  ')
        print(f'Los integrantes de la burbuja {burbuja} son, {dicci[burbuja.upper()]}')
    except KeyError:
        print("Ups! Entraste mal el nombre de la burbuja.")
        print("Hay que prestar más atención cuando se ingresan los datos! ")
        

for x in range(7):
    imprimir_integrantes(burbujas)	

        