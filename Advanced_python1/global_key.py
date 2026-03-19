a = 3 # global variable 

def my_fun():
    # local variable
    global a
    a = 54
    print(a)

my_fun()
print(a)