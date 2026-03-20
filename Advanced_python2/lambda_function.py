# def square(n):
#     return n*n
# print(square(5) )
# Instead of that we use lamda function

square = lambda n : n * n
print(square(18))

sum = lambda a,b,c : a + b + c
print(sum(1,2,3))

# Fibonacci series using  lambda function
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
n = int(input("Enter terms: "))

for i in range(n):
    print(fib(i), end=" ")


'''
DRY RUN:
-> n = 2 .fib(2-1) + fib(2-2) => fib(1) + fib(0) => 1+0=1
i runs at (2)-> 0,1
i runs at (3)-> 0,1,2 . fib(3-1)+fib(3-2) => fib(2)+fib(1) => 1+1 =>2
'''    