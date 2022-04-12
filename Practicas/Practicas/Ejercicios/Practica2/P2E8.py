import string

letras = (
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"),
    ("D","G"),
    ("B", "C", "M", "P"),
    ("F", "H", "V", "W", "Y"),
    ("K"),
    ("J", "X"),
    ("Q", "Z")
)

tabla_valores = {
    "1": letras[0],
    "2": letras[1],
    "3": letras[2],
    "4": letras[3],
    "5": letras[4],
    "8": letras[5],
    "9": letras[6],
}

palabra_ingresada = input("Ingrese una palabra: ").upper()
for c in palabra_ingresada:
    if c not in string.ascii_uppercase:
        palabra_ingresada = palabra_ingresada.replace(c,"")
while(palabra_ingresada == ""):
    palabra_ingresada = input("ERROR: PALABRA NO VÁLIDA.\nIngrese una palabra: ").upper()
    for c in palabra_ingresada:
        if c not in string.ascii_uppercase:
            palabra_ingresada = palabra_ingresada.replace(c,"")
# Repeat until?

puntos = 0
for c in palabra_ingresada:
    if(c in tabla_valores["1"]):
        puntos += 1
    elif(c in tabla_valores["2"]):
        puntos += 2
    elif(c in tabla_valores["3"]):
        puntos += 3
    elif(c in tabla_valores["4"]):
        puntos += 4
    elif(c in tabla_valores["5"]):
        puntos += 5
    elif(c in tabla_valores["8"]):
        puntos += 8
    else:
        puntos += 9

print(f"{palabra_ingresada}: {puntos} puntos.")