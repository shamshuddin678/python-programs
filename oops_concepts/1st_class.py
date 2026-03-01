'''
#Meaning of Object Instantiation in OOP's concepts:-
->Instantiation = Creating an object from a class
->When you create an object using a class, that process is called instantiation.

->Instantiation = Instance + Creation
->Instance = object
->Instantiation = creating object
'''

class Employee:
    #class Attributes
    company="Microsoft"
    language="py"
    salary=1200000

# Created an object of Employee class
shamshu = Employee()
shamshu.name="shamshuddin" # this is instance attribute
print(shamshu.company,shamshu.name,shamshu.language,shamshu.salary)
# Here name is an object attribute and company, language,salary are class attributes as they are directly belongs to class Employee method


class Coders:
    company = "Microsoft" # class attribute

ob = Coders()
ob.company = "google" # instance attribute
print(ob.company)  # it takes and prints instantce attribute 