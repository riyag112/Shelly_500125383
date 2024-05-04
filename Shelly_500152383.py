class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library")
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, Available Copies: {book['available']}")

    def add_book(self, title, author, num_copies=1):
        existing_book = next((b for b in self.books if b['title'].lower() == title.lower()), None)

        if existing_book:
            existing_book['available'] += num_copies
        else:
            new_book = {'title': title, 'author': author, 'available': num_copies}
            self.books.append(new_book)

        print(f"{num_copies} copy/copies of '{title}' added successfully to the library.")

    def search_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                print(f"Book found - Title: {book['title']}, Author: {book['author']}, Available Copies: {book['available']}")
                return
        print(f"Book with title '{title}' not found in the library.")

library = Library() 

print("Welcome to Shelly's Library!")

while True:
    print("\nLibrary Menu")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        num_copies = int(input("Enter the number of copies to add: "))
        library.add_book(title, author, num_copies)
    elif choice == '3':
        title = input("Enter the title to search: ")
        library.search_book(title)
    elif choice == '4':
        print("Exiting the Library. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
