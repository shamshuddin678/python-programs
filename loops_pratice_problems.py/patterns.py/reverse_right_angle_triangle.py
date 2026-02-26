'''
using for loop print right angle triangle in reverse order
***
**
*
'''

n=int(input("Enter a number: "))
for i in range(n,0,-1): #from n to 1
    print("*"*i,end=" ")
    print(" ")


'''
here what is happening:
for n=3
range(3,0,-1) means start from 3 to 1 with step -1-> decrementing by 1 stars
1st iteration: i=3 => ***
2nd iteration: i=2 => **
3rd iteration: i=1 => *
'''    