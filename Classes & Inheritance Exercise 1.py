class Books:
    def __init__(self, title, author, dewey, isbn):
        self.title = title
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


Books("The Lord of the Rings", "J.R.R. Tolkien", "TOL", "9780261103252")
Books("The Hunger Games", "Suzanne Collins", "COL", "978140713082")
Books("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Books("Harry Potter", "J.K. Rowling", "ROW", "9780439321624")

Users("John", "12 Example Rd", "0.0")
Users("Susan", "1011 Binary Rd", "0.0")
Users("Paul", "25 Appletree Dr", "0.0")
Users("Mary", "8 Moon Cres", "0.0")


print("------------------NEW USERS------------------")
add_user()
print("------------------USER LIST------------------")
print_user()
print("------------------NEW BOOKS------------------")
add_book()
print("------------------BOOK LIST------------------")
print_info()
