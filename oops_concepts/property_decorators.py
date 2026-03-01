class method:
    a = 1
    
    @classmethod  # decorator is used to create a class method.
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property    
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


m = method()

m.show()
m.name = " shamshuddin shaik"
print(m.name)