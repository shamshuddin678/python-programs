# adding the dyanmicall attrbutes
class Student:
    pass
s = Student()
s.name = "Shamshu"
s.age = 20
print(s.name)
print(s.age)
# retrieving dynamically using built-in methods
print(getattr(s,'name'))
print(hasattr(s,'age'))
# dynamicall changes/addds 
setattr(s,'city','Hyderabad')
print(s.city)
delattr(s,'age') # delete attribute 
