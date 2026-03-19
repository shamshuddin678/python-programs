class Car:
    color = "black"

    def show(self):
        print(f"show the color of car {self.color}")

    def display(self, name, brand):
        self.name = name
        self.brand = brand
        print(f"The name of car is {self.name} and brand is {self.brand}")

class BMW(Car):

    def showModel(self, model):
        self.model = model
        print(f"The model of the car is {self.model}")

    def printCost(self, cost):
        self.cost = cost
        print(f"The cost of car is {self.cost}")


a = Car()
a.show()
a.display("Mastang","Ford")

b = BMW()
b.show()          # inherited method
b.showModel("BMW M5")
b.printCost("2.57cr")


'''
->Feature                 ->`{name}`              ->`{self.name}`                   

->Variable Type            Local variable        Object attribute                
->Scope                    Only inside function  Stored in object                
->Lifetime                 Temporary             Exists as long as object exists 
->Access outside function  No                    Yes                           


-> important note:
if we use to {name} it is used to local variable
if we use to {self.name} it is used to object attribute
'''