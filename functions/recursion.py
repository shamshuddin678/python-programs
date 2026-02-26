#factorial=n*n-1*.....3*2*1
#factoial=n*factorial(n-1)

def fact(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
      return n*fact(n-1)

n=int(input("Enter a number: "))
print(f"factorial of n is:{fact(n)}")
# print("Factorial of n is: ", + fact(n))