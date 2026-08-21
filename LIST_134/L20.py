books = []

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)

    elif choice == 2:
        book = input("Enter book name to search: ")
        if book in books:
            print("Book found.")
        else:
            print("Book not found.")

    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("Books List:")
        for book in books:
            print(book)

    elif choice == 5:
        print("Total Books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid Choice")
