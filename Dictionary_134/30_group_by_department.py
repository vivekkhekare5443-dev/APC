students = {"Vivek": "CSE", "Tanvi": "IT", "Sanika": "CSE", "Rahul": "IT"}
departments = {}
for name, dept in students.items():
    departments.setdefault(dept, []).append(name)
print(departments)
