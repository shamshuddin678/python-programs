n=int(input("Enter a number: "))

i=1
sum=0
while(i<=n):
    sum=sum+i
    i+=1

print(sum)
# otherwise short trick to know sum=1+2+3+4=>10
'''
Here what is happening is i=1,s=0
DRY RUN ITERATIONS:
1.1<=4
s=0+1=1
i=1+1=2

2.2<=4
s=1+2=3
i=2+1=3

3.3<=4
s=3+3=6
i=3+1=4

4.4<=4
s=6+4=10
i=4+1=5
'''