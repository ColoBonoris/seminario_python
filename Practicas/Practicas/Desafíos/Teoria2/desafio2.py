cad = input("Ingrese una cadena (termina con 'FIN'): ")
while(cad != "FIN"):
    if(cad[0] == cad[-1]):
        print(cad)
    cad = input("Ingrese una cadena (termina con 'FIN'): ")