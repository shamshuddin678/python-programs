n1=int(input("Enter a number: "))

#using while loop
i=1
fact=1
while(i<=n1):
    fact=fact*i
    i+=1

print(fact) #5!=5 x4 x3x 2 x1=120

'''
DRY RUN ITERATIONS:
1.1<=5
fact=1*1=1
i=1+1=2

2.2<=5
fact=1*2=2
i=2+1=3

3.3<=5
fact=2*3=6
i=3+1=4

4.4<=5
fact=6*4=24
i=4+1=5

5.5<=5
fact=24*5=120
i=5+1=6
'''

# using for loop
n2=int(input("Enter a number: "))
f=1
for i in range(1,n2+1):
    f=f*i

print(f)