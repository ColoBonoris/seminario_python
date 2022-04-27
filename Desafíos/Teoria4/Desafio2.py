
"""
Implementar un programa que muestre un menú a través del cual se puedan visualizar los
resultados del desafío 1.
    * Pueden usar la librería console-menu analizada en clase.
    * Pueden agregar más opciones con los ejemplos mostrados en la clase.
"""

def display_menu():
    """
        Se imprime un menú y devuelve la elección de tipo entero
    """
    response_set = ("1","2","3")
    texto_menu = """

    ------------------------------------------------------
        ### Seleccione la opción a mostrar ###
    1- Todos los títulos.
    2- Todos los títulos de 2021.
    3- Los 5 países con más películas.
    0- Exit
    ------------------------------------------------------

    """
    selection = input(texto_menu)
    while(selection not in response_set):
        selection = input("\n   ### Caracter no válido!" + texto_menu)
    return(int(selection))


selection = display_menu()
ruta = os.path.realpath(".")
ruta_netflix = os.path.join(ruta, "Datos", "netflix_titles.csv")
ruta_2021 = os.path.join(ruta, "Datos", "2021_titles.csv")

while(selection != 0):
    match selection:
        case 1:
            with open() as csv_file:
        case 2:

        case 3:

    selection = display_menu()




