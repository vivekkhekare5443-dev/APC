patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 40, "O+"),
    (104, "Sneha", 28, "A+")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
search_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)
        found = True
        break

if found == False:
    print("Patient not found")

# Total number of patients
print("\nTotal patients:", len(patients))

# Display patients with a specific blood group
blood_group = input("\nEnter blood group: ")

print("Patients with blood group", blood_group + ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
