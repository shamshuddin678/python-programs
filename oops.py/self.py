class Employee:
    company="Microsoft"
    language="py"
    salary=1200000

    
    def get_details(self):
        print(f"My name is {self.name} and my company is {self.company} and my salary is {self.salary}")

    @staticmethod    
    def greet():
        print("Hello")   


shamshu = Employee() #here shamshu is object
shamshu.name="shamshuddin" #this is instance attribute
Employee.get_details(shamshu)
