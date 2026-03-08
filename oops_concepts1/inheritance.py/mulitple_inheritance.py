class Employee:
    company = "Microsoft"
    name = "shamshuddin"
    
    def show(self):
        print(f"The name of employee is {self.name} and comapny is {self.company}")

class coder:
    language = "python"
    def printLnagauge(self):
        print(f"Most programmers code in language is {self.language}")

class Programmer(Employee,coder):
    # company = "wipro"
    def showLanguge(self):
        print(f"The company of programmer is {self.company} and using language is {self.language}")

    
a = Employee()

p = Programmer()
p.showLanguge()
p.printLnagauge()
p.show()