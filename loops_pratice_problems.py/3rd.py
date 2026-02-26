# check whether numberis prime or not
num=int(input("Enter a number: "))

for i in range(2,num): #starts from 2
    if(num%i ==0): # Check if it divides perfectly
        print(" Non prime")
        break # Stop immediately because we found a factor(division=0)
else: #num%i !=0
    print("Prime") # Only runs if NO factors(division!=0) were found
