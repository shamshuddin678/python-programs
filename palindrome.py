def palindrome(n, m):
    
    # string palindrome
    if m == m[::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")

    # number palindrome
    temp = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if temp == rev:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")


n = int(input("Enter number: "))
m = input("Enter string: ")

palindrome(n, m)