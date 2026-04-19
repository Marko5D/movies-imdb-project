# Uvoz potrebhih biblioteka
import csv
import requests
from config import API_KEY


# Ucitavanje CSV fajla
def load_movies(file_path):
    movies = []

    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movies.append(row)

    return movies

# Funkcija za dobijanje podataka sa OMDb API-ja
def get_movie_data(title, year):
    url= f"http://www.omdbapi.com/?t={title}&y={year}&apikey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    if data.get("Response") == "True":
        return{
            "imdb_rating": data.get("imdbRating"),
            "actors": data.get("Actors"),
            "imdb_votes": data.get("imdbVotes")
        }
    else:
        return{
            "imdb_rating": "N/A",
            "actors": "N/A",
            "imdb_votes": "N/A"
        }
# Ucitavanje filmova iz CSV fajla
movies = load_movies("movies.csv")

print("Broj ucitanih filmova:", len(movies))
print("Prvi red:")
print(movies[0])

# Uzimamo prvi film iz liste
first_movie = movies[0]

# poziv funkcije za dobijanje podataka sa API-ja
api_data = get_movie_data(
    first_movie["title"],
    first_movie["release_year"]
)

# Dodavanje novih podataka u prvi film
first_movie.update(api_data)

# Ispis podataka koje vraca API
print("\nPRVI FILM NAKON DODAVANJA API PODATAKA:")
print(first_movie)