import string
from collections import Counter

# Separamos las letras
letras = string.ascii_lowercase
# Filtramos el string
texto = input("Ingrese una palabra o frase: ").lower()
texto_clean = texto[:]
for c in texto_clean:
    if(c not in letras):
        texto_clean = texto_clean.replace(c,"")
texto_clean = texto_clean.replace(" ","")
set_clean = set(texto_clean)
# Evaluamos la condición
if(len(texto_clean) == len(set_clean)):
    print(f"'{texto}' es un Heterograma!")
else:
    print(f"'{texto}' NO es un Heterograma.")