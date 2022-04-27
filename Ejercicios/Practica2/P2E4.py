# El texto tiene niveles de complejidad, más un boolean para título (modificable)
# Son 4 niveles de complejidad
# Los 4 niveles tienen: nombre, rango de palabras y cantidad (modificable)
# En el ejemplo dice que el texto de prueba viene con una oración fácil, pero ninguna tiene menos de 13 palabras

complexity_ranges = {
    "facil": range(1,13),
    "aceptable": range(13,18),
    "dificil": range(18,26),
    "muy_dificil": 26  
}

text_1_state = {
    "titulo": "",
    "resumen": "",
    "approved":False,
    "facil": 0,
    "aceptable": 0,
    "dificil": 0,
    "muy_dificil": 0
}

evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""
evaluar = evaluar.split("\n")
# No sé si había que sacar todos esos saltos de linea, si no hay que agregar algunas lineas

text_1_state["titulo"] = evaluar[0].replace("título: ","")
text_1_state["resumen"] = evaluar[1].replace("resumen: ","")

palabras_titulo = text_1_state["titulo"].split()
oraciones_resumen = text_1_state["resumen"].split(". ")

if(len(palabras_titulo) <= 10):
    text_1_state["approved"] = True
for i in oraciones_resumen:
    palabras = (len(i.split()))
    # Revisar las posiblilidades en el split
    if palabras in complexity_ranges["facil"]:
        text_1_state["facil"] += 1
    elif palabras in complexity_ranges["aceptable"]:
        text_1_state["aceptable"] += 1
    elif palabras in complexity_ranges["dificil"]:
        text_1_state["dificil"] += 1
    elif palabras >= complexity_ranges["muy_dificil"]:
        text_1_state["muy_dificil"] += 1

print("El titulo está aprobado." if text_1_state["approved"] else "El título está desaprobado.")
print("Tuvo {} oraciones de complejidad fácil.".format(text_1_state["facil"]))
print("Tuvo {} oraciones de complejidad aceptable.".format(text_1_state["aceptable"]))
print("Tuvo {} oraciones de complejidad difícil.".format(text_1_state["dificil"]))
print("Tuvo {} oraciones de complejidad muy difícil.".format(text_1_state["muy_dificil"]))

# dificil - Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems
# aceptable - However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization
# aceptable - Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit
# muy dificil -  We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit
# muy dificil - We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.











