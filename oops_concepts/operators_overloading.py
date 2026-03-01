# Operator overloading allows operators like +, -, *, > to work with objects of a class.
class Number:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        return self.a + other.a
    
    def __sub__(self,other):
        return self.a - other.a
    
    def __mul__(self,other):
        return self.a * other.a
    
    def __truediv__(self,other):
        return self.a / other.a
    
    def __floordiv__(self,other):
        return self.a // other.a
    
    def __mod__(self,other):
        return self.a % other.a
    
    def __gt__(self,other):
        return self.a > other.a
    
    def __lt__(self,other):
        return self.a < other.a
    
    def __eq__(self,other):
        return self.a == other.a
    
    def __ge__(self,other):  # greater than equal to
        return self.a >= other.a
    
    def __le__(self,other):  # less than equal to
        return self.a <= other.a
    
    def __ne__(self,other): # not equal to
        return self.a != other.a
    
    def __len__(self):
        return len(self.a)
    
    def __str__(self):
        return f" My name is {self.a}"
    

a = Number("shamshuddin")
print(len(a))

print(a)

a = Number(2)
b = Number(1)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)