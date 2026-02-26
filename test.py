# Multilevel_inheritance
class Animal:
    def eat(self):
        print("eating...")

class Dog(Animal):
    def bark(self):
        print("barking...")
class BabyDog(Dog):
    def weep(self):
        print("weeping...")

# Creating object of BabyDog
d = BabyDog()

d.eat()     # from Animal
d.bark()    # from Dog
d.weep()    # from BabyDog
