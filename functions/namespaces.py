# local variable -> inside the function
def test():
    x = 10
    print(x)
test()
# global varriable -> outside the function
x = 11
def test():
    print(x)
test()
# if combine both local & global
x = 10
def test():
    x = 20
    print(x)
test()
print(x)
