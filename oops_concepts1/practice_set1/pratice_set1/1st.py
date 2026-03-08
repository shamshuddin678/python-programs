class Programmer:
    company = "Microsoft"

    def __init__(self, name, language, salary):   
        self.name = name
        self.language = language
        self.salary = salary
        print("Programmer is ready")

    def get_details(self):   
        print(f"Name is {self.name}")
        print(f"Language is {self.language}")
        print(f"Salary is {self.salary}")
        print("-------------------")


# creating objects
p1 = Programmer("shamshuddin", "python", 1300000)
p2 = Programmer("raj", "java", 1300000)

# Displaying details
p1.get_details()
p2.get_details()
