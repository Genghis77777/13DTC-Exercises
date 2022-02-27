class Books:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        self.borrower = None
        book_list.append(self)

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("#############################################")


class Users:
    def __init__(self, name, address, fees):
        self.name = name
        self.address = address
        self.fees = fees
        self.books_borrowed = []
        user_list.append(self)

    def user_details(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Fees: ${self.fees}")
        print("###############################")

user_list = []


def print_user():
    for user in user_list:
        user.user_details()


def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ").title()
    fees = "0.0"
    Users(name, address, fees)
    print(f"{name} at {address}, has been added to the user list")


def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None

book_list = []


def print_info():
    for book in book_list:
        book.book_details()


def add_book():
    title = input("Enter the title of the new book: ").title()
    author = input("Enter the author of the new book: ").title()
    dewey = input("Enter the dewey of the new book: ").upper()
    isbn = input("Enter the ISBN of the new book: ")
    Books(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry, no book was found with that name")
    return None


def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.available:
            confirm = input("Type 'Y' if you want to borrow this book: ").upper()
            if confirm == "Y":
                print(f"'{book.title}' is now out on loan to {user.name}")
                book.available = False
                book.borrower = user.name
                user.books_borrowed.append(book.title)
        else:
            print(f"Sorry, '{book.title}' is already out on loan")


def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to return this book: ").upper()
            if confirm == "Y":
                print(f"'{book.title}' is now returned to the library")
                book.available = True
                book.borrower = user.name
                user.books_borrowed.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' is on loan to someone else")


Books("The Lord of the Rings", "J.R.R. Tolkien", "TOL", "9780261103252")
Books("The Hunger Games", "Suzanne Collins", "COL", "978140713082")
Books("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Books("Harry Potter", "J.K. Rowling", "ROW", "9780439321624")

Users("John", "12 Example Rd", "0.0")
Users("Susan", "1011 Binary Rd", "0.0")
Users("Paul", "25 Appletree Dr", "0.0")
Users("Mary", "8 Moon Cres", "0.0")

new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Find a user")
    print("5. Add a book")
    print("6. Find a book")
    print("7. Exit")

    choice = input("\nWhat would you like to do? \n"
                   "Enter a number: ")

    if choice == "1":
        print("------------------LEND BOOK------------------")
        lend_book()
    elif choice == "2":
        print("-----------------RETURN BOOKS----------------")
        return_book()
    elif choice == "3":
        print("------------------NEW USERS------------------")
        add_user()
    elif choice == "4":
        print("------------------FIND USER------------------")
        find_user()
    elif choice == "5":
        print("------------------NEW BOOKS------------------")
        add_book()
    elif choice == "6":
        print("------------------FIND BOOK------------------")
        find_book()
    elif choice == "7":
        confirm = input("Type 'Y' if you want to leave the system\n"
                        "Or any other key to return to the menu: ").upper()
        if confirm == "Y":
            print("Goodbye")
            new_action = False
    else:
        print("\n--- That is not a valid choice ---\n")


print("------------------USER LIST------------------")
print_user()

find_book()

add_book()

lend_book()

return_book()
print("------------------BOOK LIST------------------")
print_info()
print("---------------------END---------------------")
