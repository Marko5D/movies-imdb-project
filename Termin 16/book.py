class Book:
    def __init__(self, title, author, published, genre):
        self.title = title
        self.author = author
        self.published = published
        self.genre = genre 

    def __str__(self):
        return f"{self.title}, {self.author}, {self.published}, {self.genre}"
    

    @classmethod
    def create_from_string(cls, str):
        attributes = str.split(',')

        for i in range(len(attributes)):
            attributes[i] = attributes[i].strip()

        return cls(attributes[0], attributes[1], attributes[2], attributes[3])

