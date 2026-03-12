class Employee:
    
    @staticmethod
    def show(): # If self parameter is not used use the static method to display the function.
        print('"Hello to everyone')

e = Employee()
e.show()