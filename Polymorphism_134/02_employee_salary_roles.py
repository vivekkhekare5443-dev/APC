"""
Polymorphism - Program 2 (Role-Based Salary Polymorphism):
Create a base class Employee with a method calculate_salary().
Derive Manager, Developer, and Tester classes.
Override the method in each class to calculate salary according to the employee's role.
"""

class Employee:
    def __init__(self, emp_id, name, base_pay):
        self.emp_id = emp_id
        self.name = name
        self.base_pay = base_pay

    def calculate_salary(self):
        """Base salary calculation."""
        return self.base_pay


class Manager(Employee):
    def __init__(self, emp_id, name, base_pay, management_bonus=20000):
        super().__init__(emp_id, name, base_pay)
        self.management_bonus = management_bonus

    def calculate_salary(self):
        # Manager gets base pay + management bonus + 15% incentive
        return self.base_pay + self.management_bonus + (0.15 * self.base_pay)


class Developer(Employee):
    def __init__(self, emp_id, name, base_pay, overtime_hours=10, hourly_rate=800):
        super().__init__(emp_id, name, base_pay)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        # Developer gets base pay + overtime pay
        return self.base_pay + (self.overtime_hours * self.hourly_rate)


class Tester(Employee):
    def __init__(self, emp_id, name, base_pay, bugs_verified=25, bonus_per_bug=400):
        super().__init__(emp_id, name, base_pay)
        self.bugs_verified = bugs_verified
        self.bonus_per_bug = bonus_per_bug

    def calculate_salary(self):
        # Tester gets base pay + bug bounty allowance
        return self.base_pay + (self.bugs_verified * self.bonus_per_bug)


if __name__ == "__main__":
    employees = [
        Manager("M101", "Aarav Sharma", base_pay=60000),
        Developer("D202", "Priya Singh", base_pay=50000, overtime_hours=15),
        Tester("T303", "Rohan Verma", base_pay=40000, bugs_verified=30)
    ]

    print("=== Polymorphic Payroll Processing ===")
    for emp in employees:
        role = type(emp).__name__
        salary = emp.calculate_salary()
        print(f"[{role:<9}] {emp.name:<15} (ID: {emp.emp_id}) -> Total Salary: Rs. {salary:,.2f}")
