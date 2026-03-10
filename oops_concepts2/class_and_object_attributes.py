class Student:
    college_name = "my college" # class attribute

s = Student()
print(s.college_name)    

s.college_name = "your college" # instance or object attribute
print(s.college_name)


class Manager:
    comapany = "microsoft" # class attribute
    name = "shamshuddin"
    def __init__(self,name):
        self.name = name # object attribute

m = Manager("raju")
print(m.name)        