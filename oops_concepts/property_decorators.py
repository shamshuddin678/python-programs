class method:
    a = 1
    
    @classmethod  # decorator is used to create a class method.
    def show(cls):
        print(f"The class attribute is {cls.a}")

    '''
    ->A method with @property decorator is called getter.
    ->It is used to read/access value like a variable.not a variable it is a function without paranthesis.
    '''    
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    '''
    ->@name.setter (Setter)
    ->Setter is used to change/update value.
    '''
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


m = method()

m.show()
m.name = "shamshuddin shaik"
print(m.name) # getter 

m.name = "pro programs"
print(m.name) # setter