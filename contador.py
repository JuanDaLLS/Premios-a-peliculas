movies = {"batman": 15, "superman" : 40, "Nito y neto en la misteriosa herencia" : 50}
#### Cambiar el nombre del diccionario para que funcione
def votes_counter(movie):
    if movie in movies:
        print(f"{movies[movie]}")
    else: print("Debes elegir una opcion valida")

votes_counter("batman")