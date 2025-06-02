class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# List of books
books = [
    Books("Atomic Habits", "James Clear"),
    Books("The Alchemist", "Paulo Coelho"),
    Books("The God of Small Things", "Arundhati Roy")
]

borrowed_books = []

# Main loop
while True:
    print("\nMenu:")
    print("1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print("\nAvailable books:")
        for i, book in enumerate(books, 1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i}. {book.title} ({status})")

    elif choice == "2":
        if len(borrowed_books) >= 3:
            print("Sorry: can't borrow more than 3 books.")
            continue

        num = int(input("Enter book number to borrow: ")) - 1
        if 0 <= num < len(books):
            book = books[num]
            if not book.is_borrowed:
                book.is_borrowed = True
                borrowed_books.append(book)
                print(f"You borrowed '{book.title}'")
            else:
                print("That book is already borrowed.")
        else:
            print("Invalid number.")

    elif choice == "3":
        if borrowed_books:
            print("\nYour borrowed books:")
            for i, book in enumerate(borrowed_books, 1):
                print(f"{i}. {book.title}")
                
            num = int(input("Enter book number to return: ")) - 1
            if 0 <= num < len(borrowed_books):
                book = borrowed_books.pop(num)
                book.is_borrowed = False
                print(f"You returned '{book.title}'")
            else:
                print("Invalid number.")
        else:
            print("You haven't borrowed any books.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose a number between 1 and 4.")