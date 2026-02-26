x=int(input("Enter a number: "))

match x:
    case 0:
        print("zero")
    case 1:
        print("one")
    case _:
        print(x)