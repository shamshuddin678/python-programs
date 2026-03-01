# instance_attribute vs class_attribute
class Employee1:
    language="python"  #class attribute
    salary=100000

py=Employee1()
py.language="java"  #instance attribute
print(py.language)    