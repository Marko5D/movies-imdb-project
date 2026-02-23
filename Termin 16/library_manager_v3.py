from book import Book

print("=== Library Manager ===")

while True:
    print("1) Show books")
    print("2) Add a new book")
    print("3) Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        print("\All books:")
        text_file = open("books.txt", "r", encoding="utf-8")
        text_file_content = text_file.read()
        print(text_file_content)


    elif choice == "2":
        book_title = input('Book title:')
        book_author = input('Book author:')
        book_published = input('Year of publishing:')
        book_published = int(book_published)
        book_genre = input('Book genre:')

        book = Book(book_title, book_author, book_published, book_genre)

        text_file = open("books.txt", "a", encoding="utf-8")
        text_file.write(f"{book}\n")
        text_file.close()

    elif choice == "3":
        print("\nGoodbye!")
        break