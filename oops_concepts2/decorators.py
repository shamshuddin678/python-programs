class Student:
    college_name = "our college"

    def __init__(self,name,marks):
        self.name = name
        self._marks = marks
        print(f"the student name is {self.name} and marks are {self.marks}")
    
    def welcome(self): # method
        print("Hello to everyone")

    # def get_marks(self):
    #     return self.marks instead of writing of get_marks()
    # we use decorators
    @property
    def marks(self):
        return self._marks    

s = Student("shmashuddin",89)
s.welcome()
print(s.marks)     