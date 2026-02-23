from book import Book
import csv

print("=== Library Manager ===")

while True:
    print("1) Show books")
    print("2) Add a new book")
    print("3) Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        print("\All books:")
        with open('books.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                book = Book(**row)
                print(book)

    elif choice == "2":
        book_title = input('Book title:')
        book_author = input('Book author:')
        book_published = input('Year of publishing:')
        book_published = int(book_published)
        book_genre = input('Book genre:')

        book = Book(book_title, book_author, book_published, book_genre)

        with open('books.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames=["title", 'author', 'published', 'genre']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(book.__dict__)


    elif choice == "3":
        print("\nGoodbye!")
        break