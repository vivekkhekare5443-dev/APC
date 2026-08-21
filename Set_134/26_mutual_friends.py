user1 = {"Amit", "Rahul", "Priya", "Sneha"}
user2 = {"Rahul", "Sneha", "Riya", "Kiran"}

print("Mutual friends:", user1 & user2)
print("Unique to User 1:", user1 - user2)
print("Unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)
