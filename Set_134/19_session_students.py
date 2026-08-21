morning = {"Amit", "Rahul", "Priya", "Sneha"}
afternoon = {"Rahul", "Sneha", "Riya", "Kiran"}

print("Both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one:", morning | afternoon)
