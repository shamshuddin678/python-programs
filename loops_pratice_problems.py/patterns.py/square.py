'''
for j in  range(5):
    print("*",end=" ")

print()  -> Move to the next line
for j in range(5):
    print("*",end=" ")  
output:
* * * * *
* * * * *     
'''
'''NOTE:
1.In the above code we are writing same for loop again .
2.To avoid this we can use nested loops.
means that 2nd loop write inside the 1st loop.
'''
n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print("#",end=" ") #-> if we don't use end=" " inside space means ""(it prints rectangle pattern)
    print(" ")  #move to next line after inner loop ends    