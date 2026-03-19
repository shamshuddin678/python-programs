'''
Type definitons in python:
a : int 3
b : int 4
it representing the its data type
'''
def sum(a : int,b : int) -> int:
    # print(F"The sum is {a + b}")
    return a + b
print(sum(2,3))

def string(emp_name : str, emp_role : str) -> str:
    print(f"The employee name is {emp_name} and role is {emp_role}")
string("shamshuddin","python developer")    