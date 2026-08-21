contacts = {}
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        contacts[input("Enter name: ")] = input("Enter phone: ")
    elif choice == 2:
        print(contacts.get(input("Enter name: "), "Contact not found"))
    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts: contacts[name] = input("Enter new phone: ")
    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts: del contacts[name]
    elif choice == 5:
        for name, phone in contacts.items(): print(name, ":", phone)
    elif choice == 6:
        break
