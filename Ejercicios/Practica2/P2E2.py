from collections import Counter

texto = """The constants defined in this module are:The constants defined in␣
    →this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
    →described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
    →locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
    →locale-dependent and will not change.
"""
# lista con todas las palabras
words = (texto.lower().split())
# lista con palabras sin repetir
word_set = (set(words))

contador = Counter(words)
print(f"###     '{contador.most_common(1)[0][0]}' es la palabra con más apariciones ({contador.most_common(1)[0][1]} en total).")


