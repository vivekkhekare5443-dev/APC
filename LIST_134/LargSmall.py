nums = [45, 12, 89, 5, 67]

largest = smallest = nums[0]

for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
