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

    return data
# Ucitavanje filmova iz CSV fajla
movies = load_movies("movies.csv")

print("Broj ucitanih filmova:", len(movies))
print("Prvi red:")
print(movies[0])

first_movie = movies[0]
# poziv funkcije za dobijanje podataka sa API-ja
api_data = get_movie_data(
    first_movie["title"],
    first_movie["release_year"]
)

# Ispis podataka koje vraca API
print("\nAPI PODACI:")
print(api_data)