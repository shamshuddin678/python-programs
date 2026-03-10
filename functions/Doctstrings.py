''' 
->Doctstring(Documentation string) write inside triple quotes.
->uthat explains what a module,class,function,method
''' 
# 1.Function Doctstring
def square(n):
    '''It takes the n value and perform the square operation'''
    return n**2

print(square(5))
print(square.__doc__)

# 2.class Doctstring
class Doctstring:
    '''The Doctsring method is using in the class'''
print(Doctstring.__doc__)

'''
Note:
function_name.__doc__
class_name.__doc__
module_name.__doc__
'''