from book import Book

text_file = open("books.txt", "r", encoding="utf-8")

books = []

for line in text_file:
    line = line.strip()
    books.append(Book.create_from_string(line))
text_file.close()


while True:

    command = input('Add new (y/n)?')
    if(command == 'n'):
        break

    book_title = input('Book title:')
    book_author = input('Book author:')
    book_published = input('Year of publishing:')
    book_published = int(book_published)
    book_genre = input('Book genre:')

    book = Book(book_title, book_author, book_published, book_genre)
    books.append(book)
    print(f'You have entered: {book}')

text_file = open("books.txt", "w", encoding="utf-8")

for book in books:
    print(book)
    text_file.write(f"{book}\n")

print('Goodbye!')
