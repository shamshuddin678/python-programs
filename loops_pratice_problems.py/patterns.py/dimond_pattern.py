'''
  *    1
 ***   2
*****  3 (upto here for loop 1:(1,n+1))
 ***   2 -> for loop 2: (n-1,0,-1)=> (3-1=2 to 1)
  *    1->step_size -1
'''
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ") #move to new line
for i in range(n-1,0,-1):    
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ") #move to new line