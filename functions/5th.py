def pattern(n):
    if n==0:
        return "no pattern available"
    else:
      print("$" * n)
      pattern(n-1)

n=int(input("Enter a number: "))
print(pattern(n))        
