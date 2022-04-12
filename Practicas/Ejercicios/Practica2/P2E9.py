def analizar_casilla(celda,pos_l,pos_c):
    # recibe la celda, pero evalúa la situación de una casilla
    cercanas = 0
    len_linea = len(celda[0])
    match pos_l:
        case 0:
            match pos_c:
                case 0:
                    if(celda[pos_l][pos_c + 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c + 1] == "*"):
                        cercanas += 1
                case len(celda[pos_l]):
                    if(celda[pos_l][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c - 1] == "*"):
                        cercanas += 1
                case _:
                    if(celda[pos_l][pos_c + 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[pos_l][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l + 1)][pos_c + 1] == "*"):
                        cercanas += 1
        case len(pos_c):
            match pos_c:
                case 0:
                    if(celda[pos_l][pos_c + 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c + 1] == "*"):
                        cercanas += 1
                case len(celda[pos_l]):
                    if(celda[pos_l][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c - 1] == "*"):
                        cercanas += 1
                case _:
                    if(celda[pos_l][pos_c + 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c] == "*"):
                        cercanas += 1
                    if(celda[pos_l][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c - 1] == "*"):
                        cercanas += 1
                    if(celda[(pos_l - 1)][pos_c + 1] == "*"):
                        cercanas += 1
        case _:
            if(celda[pos_l][pos_c + 1] == "*"):
                cercanas += 1
            if(celda[(pos_l - 1)][pos_c] == "*"):
                cercanas += 1
            if(celda[pos_l][pos_c - 1] == "*"):
                cercanas += 1
            if(celda[(pos_l - 1)][pos_c - 1] == "*"):
                cercanas += 1
            if(celda[(pos_l - 1)][pos_c + 1] == "*"):
                cercanas += 1
            if(celda[(pos_l + 1)][pos_c] == "*"):
                cercanas += 1
            if(celda[(pos_l + 1)][pos_c - 1] == "*"):
                cercanas += 1
            if(celda[(pos_l + 1)][pos_c + 1] == "*"):
                cercanas += 1
    return cercanas

def analizar_celda(celda):
    # recibe la celda y envía la información necesaria para que se analice una casilla y la modifica
    # Puede forzarse el tipo?
    len_linea = len(celda[0])
    for pos_l in range(0,len(celda),1):
        for pos_c in range(0,len_linea,1):
            cercanas = analizar_casilla(celda,pos_l,pos_c)
            celda[pos_l] = (celda[pos_l][0:pos_c]) 
            + str(cercanas)
            + (celda[pos_l][(pos_c + 1),len_linea])
            # ahora tiene que modificarse la casilla

# Puede extenderse a celdas más grandes y más chicas
# las únicas excepciones son alto/ancho = 1
# me gustaría generalizar un poco la evaluación de casilla, capaz con alguna lambda,
# o con funciones definidas, hay que ver

celda = [
'-*-*-',
'--*--',
'----*',
'*----',
]

celda_modificada = analizar_celda(celda)
print(celda_modificada)
