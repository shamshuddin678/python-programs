'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class Demo:
    a=4 #class attribute

object = Demo()
print("Before changing class attribute")
print(f"Class attribute: {Demo.a}")
print(f"Object attribute: {object.a}") # prints the class attribute .because the instance attribute is not present 
print("---------")

# changing the class attribute using object
object.a=0 # Here instance attribute is set 
print("After changing class attribute")
print(f"Object attribute: {object.a}")  # print the instance attribute.because the instance attribute is present 
print(f"class attribute: {Demo.a}") # prints the class attribute

# Answer is class attribute is not changed