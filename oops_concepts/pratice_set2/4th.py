class Complex:

    def __init__(self,n,i):
        self.n = n
        self.i = i

    def __add__(self,c1):
        return (self.n + c1.n , self.i + c1.i)

    def __str__(self):
        return f"{self.n} + {self.i}"


'''Here self.n = 2, self.i = 2 and c1.n = 1, c1.i = 2
the operation perform is {self.n + c1.n , self.i + c1.i} it returns the 
{1 + 2 ,2i + 3i} = {3 + 5i} complex number is 3 + 5j
'''
c1 = complex(1,2)
c2 = complex(2,3)

print(f"The complex number is {c1 + c2}")