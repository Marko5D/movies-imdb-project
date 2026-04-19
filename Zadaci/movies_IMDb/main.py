# Uvoz potrebhih biblioteka
import csv
import requests
import time
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

# Dodavanje API podataka svim filmovima
def enrich_movies(movies):
    for movie in movies:
        api_data = get_movie_data(
            movie["title"],
            movie["release_year"]
        )

        movie.update(api_data)
        time.sleep(1)

    return movies

# Glavni deo programa
movies = load_movies("movies.csv")

print("Broj ucitanih filmova:", len(movies))

movies = enrich_movies(movies)

# Ispis podataka koje vraca API
print("\nPRVI FILM NAKON OBRADE:")
print(movies[0])