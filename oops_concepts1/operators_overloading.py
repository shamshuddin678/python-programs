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


# Assignment operator overloading
class Number1:
    def __init__(self, x):
        self.x = x
    def __iadd__(self, other):
        self.x += other
        print(f"the iadd operator {self.x}")
        return self
    def __isub__(self, other):
        self.x -= other
        print(f"the isub operator {self.x}")
        return self
    def __imul__(self, other):
        self.x *= other
        print(f"the imul operator {self.x}")
        return self   
n1 = Number1(13)

n1 += 13
n1 -= 1
n1 *= 2

# Uninary operator overloading
class Number2:
    def __init__(self,s):
        self.s = s
    def __neg__(self):
        return f"The negative {-self.s}"    
    def __pos__(self):
        return f"The positive {+self.s}"    
    def __abs__(self):
        return f"The absolute {self.s}"

ob = Number2(99)
print(-ob)
print(+ob)
print(abs(ob))