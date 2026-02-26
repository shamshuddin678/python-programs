n=int(input("Enter a number: "))

for i in range(1,n+1):
    if(i==1 or i % 2!=0):
        print("** **")
    else:
        print("*** ***")
    print("-"*i)    