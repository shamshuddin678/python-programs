l = list(map(int,input("Enter list: ").split()))
print(l)

t = tuple(map(int,input("Enter tuple: ").split()))
print(t)

# set
s = set(map(int,input("Enter set: ").split()))
print(s)

# Dictionary
dict = {}
n = int(input("Enter no of items: "))

for _ in range(n):
    key,value = input("Enter key value: ").split()
    dict[key] = value

print(dict)    