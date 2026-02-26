# fibonacci seqeuence: 0 1 1 2 3 5 8 13 21 .....
#                      0 1 2 3 4 5 6  7  8                          

def fibo(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


n=int(input("Enter a number: "))
print(fibo(n))    

'''
DRY RUN:
n=3
fibo(3)=fibo(2)+fibo(1) => fibo(2)=fibo(1)+fibo(0)=1+0=1
fibo(3)=1+1=2


'''