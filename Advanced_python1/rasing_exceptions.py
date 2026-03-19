a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(b == 0):
    raise ZeroDivisionError("Hello our program not meant by divising" \
    "zeros it rasing the exception")
else:
    print(f"The division occurs and value is {a / b} ")