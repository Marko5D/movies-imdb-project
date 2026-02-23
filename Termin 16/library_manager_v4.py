from book import Book
import pickle
import os

print("=== Library Manager ===")

my_books = []

if os.path.exists('books.pkl'):
    with open('mbooks.pkl', 'rb') as file:
        my_books = pickle.load(file)

while True:
    print("1) Show books")
    print("2) Add a new book")
    print("3) Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
       print('\All books:')
       for book in my_books:
           print(book)


    elif choice == "2":
        book_title = input('Book title:')
        book_author = input('Book author:')
        book_published = input('Year of publishing:')
        book_published = int(book_published)
        book_genre = input('Book genre:')

        book = Book(book_title, book_author, book_published, book_genre)

        my_books.append(book)

        with open('books.pkl', 'wb') as file:
            pickle.dump(my_books, file)


    elif choice == "3":
        print("\nGoodbye!")
        break