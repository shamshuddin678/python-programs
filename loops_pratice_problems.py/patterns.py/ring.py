'''
***
* *
* *
'''
n=int(input("Enter a value: "))


for i in range(1,n+1):
    if(i==1 or i==n):
       print("*"*n)
    else:
        #Middle rows: first star + spaces + last star
      print("*",end="")
      print(" "*(n-2),end="")
      print("*",end="")
      print(" ")