# constructors and destructors
class Employee:

    def __init__(self, role, salary):   # constructor
        print("Adding the Employee to the database mysql....")
        self.role = role
        self.salary = salary

    def show(self):  # function
        return f"The employee role is {self.role} and salary is {self.salary}"

    def __del__(self):   # destructor
        print(f"Employee object destroyed")


e = Employee("Junior python developer", "15LPA")
print(e.show())