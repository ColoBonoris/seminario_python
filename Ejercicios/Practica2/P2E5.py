texto = input("Ingrese una oración: ").lower()
palabra_busqueda = input("Ingrese un string a buscar: ").lower()
# Saco apariciones de caracteres que no sean letra, capaz (seguro) haya una forma más rápida
texto = texto.replace(".","")
texto = texto.replace(",","")
texto = texto.replace(";","")
texto = texto.replace(":","")
texto = texto.replace("¿","")
texto = texto.replace("?","")
texto = texto.replace("!","")
palabras = texto.split()
apariciones = palabras.count(palabra_busqueda)
print(f"Hubieron {apariciones} apariciones de '{palabra_busqueda}' en el texto.")