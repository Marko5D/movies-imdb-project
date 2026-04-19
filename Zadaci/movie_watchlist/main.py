import os
import pickle
from movie import Movie

FILE_NAME = "movies.pkl"

def load_movies():
    """Ucitava filmove iz fajla. Ako fajl ne postoji ili je prazan,
      vraca praznu listu."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "rb") as file:
            movies = pickle.load(file)
            return movies
    except (EOFError, pickle.PickleError):
        return []
    

def save_movies(movies):
    """Cuva listu filmova u fajl."""
    with open(FILE_NAME, "wb") as file:
        pickle.dump(movies, file)


def input_release_year():
    """Trazi od korisnika validnu godinu izlaska."""
    while True:
        year = input("Movie release year: ").strip()

        if year.isdigit():
            return int(year)
        
        print("Invalid input. Please enter a valid year.")


def add_movies():
    """Unos novog filma."""
    movies = load_movies()

    print("\n--- Add new movie ---")
    title = input("Movie title: ").strip()
    release_year = input_release_year()
    genre = input("Movie genre: ").strip()
    imdb_url = input("Add IMDb URL: ").strip()

    new_movie = Movie(title, release_year, genre, imdb_url)
    movies.append(new_movie)

    save_movies(movies)
    print("Movie successfully added.\n")


def show_all_movies():
    """Prikaz svih unetih filmova."""
    movies = load_movies

    print("\n--- Show all movies ---")
    if not movies:
        print("There are no saved movies.\n")
        return
    
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}\n")


def show_menu():
    """Prikaz menija."""
    print("***WELCOME TO THE MOVIE WATCHLIST APP***")
    print("Add new movie(1)")
    print("Show all movies(2)")
    print("Exit(3)")


def main():
    """Glavna funkcija programa."""
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movies()
        elif choice == "2":
            show_all_movies()
        elif choice == "3":
            print("Have a nice day!")
            break
        else:
            print("Invalid option. Please choose 1,2 or 3.\n")


if __name__ == "__main__":
    main()