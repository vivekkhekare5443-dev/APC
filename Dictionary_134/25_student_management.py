students = {"Vivek": 90, "Tanvi": 85}
while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Display 6.Highest 7.Average 8.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        students[input("Enter name: ")] = int(input("Enter marks: "))
    elif choice == 2:
        name = input("Enter name: ")
        if name in students: students[name] = int(input("Enter new marks: "))
        else: print("Student not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in students: del students[name]
        else: print("Student not found")
    elif choice == 4:
        name = input("Enter name: ")
        print(students.get(name, "Student not found"))
    elif choice == 5:
        print(students)
    elif choice == 6 and students:
        name = max(students, key=students.get)
        print(name, students[name])
    elif choice == 7 and students:
        print("Average:", sum(students.values()) / len(students))
    elif choice == 8:
        break
