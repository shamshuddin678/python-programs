class Employee:
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3

o = Employee()
print(o.a) # Here it prints a value 1
# print(o.b) # Here it shows error beacuse b is not present in class Employee           

o = programmer()
print(o.a,o.b) # Here it prints a and b values 


o = Manager()
print(o.a,o.b,o.c) # Here it prints a,b,c values