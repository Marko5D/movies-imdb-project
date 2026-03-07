from book import Book
import pandas as pd

print("=== Library Manager ===")

while True:
    print("1) Show books")
    print("2) Add a new book")
    print("3) Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        print("All books:")
        df = pd.read_csv('books.csv')
        print(df.to_string())


    elif choice == "2":
        book_title = input('Book title:')
        book_author = input('Book author:')
        book_published = input('Year of publishing:')
        book_published = int(book_published)
        book_genre = input('Book genre:')

        book = Book(book_title, book_author, book_published, book_genre)

        df = pd.DataFrame([book.__dict__])

        df.to_csv('books.csv', index=False, header=False, mode="a", encoding='utf-8')

    elif choice == "3":
        print("\nGoodbye!")
        break