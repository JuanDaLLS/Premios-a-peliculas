peliculas = {}
categorias = ("terror", "accion", "comedia")

def Mostrar_peli():
    print("\nPelículas registradas:")
    for nombre, datos in peliculas.items():
        print("*" * 20)
        print(f"Nombre: {nombre}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Votos: {datos['votos']}")

def registro_pelicula():
    nombre = input("Ingrese el nombre de la película: ").strip()
    categoria = input("Ingrese la categoría de la película (terror, accion, comedia): ").strip().lower()
    
    if categoria not in categorias:
        print("Categoría inválida.")
        return
    
    peliculas[nombre.lower()] = {
        "categoria": categoria,
        "votos": 0
    }
    print(f"Película '{nombre}' registrada correctamente.")
    Mostrar_peli()

def registrar_voto():
    if not peliculas:
        print("No hay películas registradas.")
        return

    Mostrar_peli()
    pq_votar = input("Escriba el nombre de la película que desea votar: ").strip().lower()
    
    if pq_votar in peliculas:
        peliculas[pq_votar]["votos"] += 1
        print(f"¡Gracias! Voto registrado para '{pq_votar}'. Total: {peliculas[pq_votar]['votos']}")
    else:
        print("No se encontró la película.")

def votes_counter():
    movie = input("Ingrese el nombre de la película que quiere revisar: ").strip().lower()
    if movie in peliculas:
        print(f"La película '{movie}' lleva {peliculas[movie]['votos']} votos a favor.")
    else:
        print("Película no encontrada.")

def winner():
    if not peliculas:
        print("No hay películas para evaluar.")
        return
    max_votes = -1
    peli_ganadora = ""
    for nombre, datos in peliculas.items():
        if datos["votos"] > max_votes:
            max_votes = datos["votos"]
            peli_ganadora = nombre
    print(f"\n🎉 La película ganadora es '{peli_ganadora}' con {max_votes} votos.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1) Registrar película")
        print("2) Ver películas")
        print("3) Registrar voto")
        print("4) Consultar votos por película")
        print("5) Ver ganadora")
        print("6) Salir")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            registro_pelicula()
        elif opcion == "2":
            Mostrar_peli()
        elif opcion == "3":
            registrar_voto()
        elif opcion == "4":
            votes_counter()
        elif opcion == "5":
            winner()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


menu()
