books = {}


def add_book(book_id, name):
    books[book_id] = {
        "name": name,
        "available": True
    }


def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")


def search_book(name):
    for book_id, book in books.items():
        if name.lower() in book["name"].lower():
            print(book_id, book["name"])


def display_available():
    print("\nAvailable Books:")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["name"])


add_book(1, "Python Programming")
add_book(2, "Data Structures")
add_book(3, "Cloud Computing")

search_book("Python")
issue_book(1)
display_available()
return_book(1)
display_available()