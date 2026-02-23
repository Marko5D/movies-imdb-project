from book import Book

books = []

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

for book in books:
    print(book)

print('Goodbye!')
