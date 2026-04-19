class Movie:
    def __init__(self, title, release_year, genre, imdb_url):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.imdb_url = imdb_url

    def __str__(self):
        return(
            f"(self.title), (self.release_year)\n"
            f"(self.genre)\n"
            f"(self.imdb_url)\n"
        )