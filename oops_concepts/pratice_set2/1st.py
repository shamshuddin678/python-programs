'''
Create a class (2-D vector) and use it to create another 
class representing a 3-D vector.'''

class TwoDVecctor:

    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2d vector is {self.i}i + {self.j}j")

class ThreeDVecctor(TwoDVecctor):
    
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"3d vector is {self.i}i + {self.j}j + {self.k}k")

v = TwoDVecctor(1,2)
v.show()

v = ThreeDVecctor(1,2,3)
v.show()
    