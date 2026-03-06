'''
Create a class 'Employee' and add salary and increment properties to it.
Write a method 'salaryAfterIncrement' method with a @property decorator with a setter
which changes the value of increment based on the salary.
'''

class Employee:
    salary = 365
    increment = 35

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        '''
        increment % = (new salary - old salary) / old salary * 100 
        -> Here we also use the short formula. divide the old salary by new salary and old salary
        -> The formula is incerment % = (new salary / old salary) - 1) * 100
        ''' 
        self.increment = ((new_salary / self.salary) - 1)* 100


e = Employee()

print("Old salary after increment:", e.salaryAfterIncrement)

e.salaryAfterIncrement = 500   # setter works   

print("New increment:", e.increment)
print("New salary:", e.salaryAfterIncrement)