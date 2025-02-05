class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display_employee_info(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: ${self.salary}\nDepartment: {self.department}\n")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, team_size=0):
        super().__init__(name, employee_id, salary, department)
        self.team_size = team_size
        self.team_members = []

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Team Size: {self.team_size}")
        print("Team Members:", ", ".join(self.team_members) if self.team_members else "No team members yet", "\n")

    def add_team_member(self, name):
        self.team_members.append(name)
        self.team_size += 1
        print(f"{name} has been added to your team.\n")

    def remove_team_member(self, name):
        if name in self.team_members:
            self.team_members.remove(name)
            self.team_size -= 1
            print(f"{name} has been removed from your team.\n")
        else:
            print(f"{name} is not in your team.\n")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to ${self.salary}.\n")

emp = Employee("Alice Johnson", "E123", 50000, "Finance")
emp.display_employee_info()

mgr = Manager("Bob Smith", "M456", 80000, "Engineering")
mgr.display_manager_info()

mgr.add_team_member("Charlie Brown")
mgr.add_team_member("David Green")
mgr.display_manager_info()

mgr.remove_team_member("Charlie Brown")
mgr.update_salary(85000)
mgr.display_manager_info()
