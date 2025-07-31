movies = {
    "batman": 15,
    "superman": 40,
    "Nito y neto en la misteriosa herencia": 50,
    "puro mula": 12
}

def winner():
    winnervotes = 0
    winner_movie = ""
    for movie in movies:
        votes = movies[movie]
        if votes > winnervotes:
            winnervotes = votes
            winner_movie = movie
    print(f"La película ganadora es: "
          f"\n{winner_movie}' con {winnervotes} votos.")

winner()
