class Employee:
    company = "Microsoft"
    language = "py"
    salary = 1200000

    # here double underscore init constructor
    def __init__(self,name,comapny,salary,language): #dunder method automatically called 
        self.name = name
        self.company = comapny
        self.salary = salary
        self.language = language
        print("Employee is ready")

    def get_details(self):
        print(
            f"My name is {self.name} and my company is {self.company} and my salary is {self.salary}"
            )

shamshu = Employee("shamshuddin","Microsoft",1300000,"python")
# print(shamshu.name,shamshu.company,shamshu.salary)
# print(f"{shamshu.name}\n{shamshu.company}\n{shamshu.salary}") here step by step \n using another method is below
print(shamshu.name,shamshu.company,shamshu.salary,shamshu.language,sep="\n")
