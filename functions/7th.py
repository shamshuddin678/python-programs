def multiplication_table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
    return 'Thanks '

n=int(input("Enter a number to print its multiplication table: "))
print(multiplication_table(n))        