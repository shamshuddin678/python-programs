class Employee:
    company = "Microsoft"
    
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of employee is {self.name} and salary is {self.salary}")
    
class Programmer(Employee):
    company = "wipro"
    def show(self,name,language):
        self.name = name
        self.language = language
        print(f"The name is {self.name} and language is use by programmer {self.language}")

    
obj = Employee()
print(obj.company)
obj.show("raju",50000)

obj1 = Programmer()
print(obj1.company)
obj1.show("shamshuddin","python")