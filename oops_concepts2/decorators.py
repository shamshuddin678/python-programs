class Decorator:
    company = "Microsoft"
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self,value):
        self._name = value

d = Decorator("shamshuddin")
print(f"Here using getter decorator @property,so name is {d.name} (name is not changing)")   # propert means no need to change it printing the 
d.name = "shaik shamshuddin" 
print(f"Here using setter decorator @function_name.setter,so name is {d.name} (changing)")   # Setter means changing the property     