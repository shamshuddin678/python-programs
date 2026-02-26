class Employee:
    company = "Microsoft"
    def show(slf):
        print(f"The name of employee is {slf.name} and salary is {slf.salary}")
    

class Programmer(Employee):
    company = "wipro"
    def show(slf,name,salary,language):
        slf.name = name
        slf.salary = salary
        slf.language = language
        print(f"The language is use by programmer {slf.language}")

    
obj = Employee()
obj1 = Programmer()


print(obj.company) 
print(obj1.company)