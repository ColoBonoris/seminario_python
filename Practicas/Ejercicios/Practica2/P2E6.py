frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
frase = frase.replace("\n"," ")
frase = frase.lower()
frase = frase.split()
frase = set(frase)
frase = list(frase)
# Pide una lista especificamente, por eso el casting
# Podríamos hacerlo con una linea sola como la seguiente pero se me hace muy feo 
# frase = list(set(frase.replace("\n"," ").lower().split()))
print(frase)