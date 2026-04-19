import csv

def load_movies(file_path):
    movies = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)

    return movies

movies = load_movies("movies.csv")

print("Broj ucitanih filmova:", len(movies))
print("Prvi red:")
print(movies[0])