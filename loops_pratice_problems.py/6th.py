n=int(input("Enter a number: "))

for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ")

'''
DRY RUN ITERATIONS:
1.n=3
  *(n-1=3-1=>2spaces)
 ***(2*i-1=>2*2-1=>4-1=>3 stars)
*****(n-i=>3-3=>0spaces)
'''
  

'''
for n=3 
  *
 ***
*****
'''