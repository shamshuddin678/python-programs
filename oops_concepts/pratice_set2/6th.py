class Vector:

    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self):
        return (self.i + self.j + self.k)

    def __str__(self):
        return f" {self.i}i + {self.j}j + {self.k}k"
    
v = Vector(1,2,3)

print(v)
