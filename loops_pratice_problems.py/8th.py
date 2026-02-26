n=int(input("Enter a number: "))

for i in range(1,n+1):
    if(i==1 or i==n): #first row or last row
       print("*"*n)
       
    else:
         #Middle rows: first star + spaces + last star
        #   print("*" + " " * (n - 2) + "*")   
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print(" ")



'''
***
* * for n = 3
***
'''    