books = {}
while True:
    print("\n1.Add 2.Search 3.Remove 4.Display 5.Count 6.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        books[input("Enter book ID: ")] = input("Enter book name: ")
    elif choice == 2:
        print(books.get(input("Enter book ID: "), "Book not found"))
    elif choice == 3:
        book_id = input("Enter book ID: ")
        if book_id in books: del books[book_id]
    elif choice == 4:
        print(books)
    elif choice == 5:
        print("Total books:", len(books))
    elif choice == 6:
        break
