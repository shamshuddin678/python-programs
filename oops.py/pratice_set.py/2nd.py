class Calculaor:

    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"{self.n**2}")

    def cube(self):
        print(f"{self.n**3}")
    
    def sqaure_root(self):
        print(f"{self.n**1/2}")           

a = Calculaor(4 )
a.square()
a.cube()
a.sqaure_root()