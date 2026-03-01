class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class programmer(Employee):
    def __init__(self):
        print("Constructor of programmer")
        super().__init__()
    b = 2

class Manager(programmer):
    def __init__(self):
        print("Constructor of Manager")
        # super() method is used to access the methods of a super class in the derived class.
        super().__init__()  
    c = 3

# o = Employee()
# print(o.a) # Here it prints a value 1
# # print(o.b) # Here it shows error beacuse b is not present in class Employee           

o = programmer()
print(o.a,o.b) # Here it prints a and b values 


o = Manager() # Here runs only 1 constructor if we want to run the parent constructor use super method above in manager 
print(o.a,o.b,o.c) # Here it prints a,b,c values