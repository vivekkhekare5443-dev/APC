names = []
ages = []

while True:
    print("\n1. Add Patient")
    print("2. Delete Patient")
    print("3. Search Patient")
    print("4. Display All Patients")
    print("5. Count Total Patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        names.append(name)
        ages.append(age)

    elif choice == 2:
        name = input("Enter patient name to delete: ")
        if name in names:
            index = names.index(name)
            names.pop(index)
            ages.pop(index)
            print("Patient deleted.")
        else:
            print("Patient not found.")

    elif choice == 3:
        name = input("Enter patient name to search: ")
        if name in names:
            index = names.index(name)
            print("Patient Found")
            print("Name:", names[index])
            print("Age:", ages[index])
        else:
            print("Patient not found.")

    elif choice == 4:
        print("\nPatient List:")
        for i in range(len(names)):
            print(names[i], "-", ages[i])

    elif choice == 5:
        print("Total Patients:", len(names))

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")
