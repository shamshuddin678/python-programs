'''Create the student class that takes name& marks of 3 
subjects as arguments in constructor.then create a method to print
the average
'''

class Student:
    
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3) / 3
        print(f"Hello, {self.name} and your average score {avg}")

s = Student("shamshuddin",1,2,3)
s.average()