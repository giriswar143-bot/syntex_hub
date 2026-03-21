class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def show_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\n--- Library Collection ---")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_issued:
                    book.is_issued = True
                    print(f"You have successfully issued '{book.title}'.")
                    return
                else:
                    print("Sorry, this book is already issued.")
                    return
        print("Book not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    book.is_issued = False
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print("This book was not issued.")
                    return
        print("Book not found.")

# --- Main Program Loop ---
def main():
    my_library = Library()
    
    # Adding some initial books
    my_library.add_book("Python Crash Course", "Eric Matthes")
    my_library.add_book("Clean Code", "Robert C. Martin")

    while True:
        print("\n1. View Books\n2. Add Book\n3. Issue Book\n4. Return Book\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.show_books()
        elif choice == '2':
            t = input("Enter Book Title: ")
            a = input("Enter Author: ")
            my_library.add_book(t, a)
        elif choice == '3':
            t = input("Enter book name to issue: ")
            my_library.issue_book(t)
        elif choice == '4':
            t = input("Enter book name to return: ")
            my_library.return_book(t)
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
