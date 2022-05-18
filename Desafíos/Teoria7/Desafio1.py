mi_musica = {70: ["Stairway to heaven", "Bohemian Rhapsody"],
    80: ["Dancing in the dark", "Welcome to the jungle", "Under pressure"],
    2000:["Given up", "The pretender"]}
tema = input("Ingresá un nuevo tema (FIN para terminar): ")
while tema != "FIN":
    try:
        decada = int(input("ingresá a qué década pertenece: ")) # ValueError acá
        mi_musica[decada].append(tema) # KeyError acá
    except ValueError:
        print("### La década debe ser un número!")
    except KeyError:
        mi_musica[decada] = [tema]
    tema = input("Ingresá un nuevo tema (FIN para terminar): ")

print(mi_musica)