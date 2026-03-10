# Palindrome substring
n = int(input("Enter number: "))
s = input("Enter string: ")

ans = ""

for i in range(n):
    for j in range(i, n):
        t = s[i:j+1]
        if t == t[::-1]:
            if len(t) > len(ans) or (len(t) == len(ans) and t < ans):
                ans = t

print(len(ans))
print(ans)

'''
n = 3, s = 'aapaa'
range(0,3):
t = s[0 : 0+1] => s[0 : 1] => a
if a == a:
   if 0 > 0 or 0 == 0 and a < ans:
   ans = a 
'''