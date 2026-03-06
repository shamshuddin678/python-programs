# set is a mutable. but frozenset is immutable

# set
s = set()

for i in range(1,6):
    n = int(input("Enter n: "))
    s.add(n)

print(s)       

# Creating a frozenset
a = frozenset([1, 2, 3, 4])  # Here the list [1,2,3,4] is converted into a frozenset.
print(a) 

'''
->Using sets as dictionary keys
->Protecting data from modification
'''
a = frozenset([1,2,3])
b = frozenset([4,5,6])

d = {a: "first", b: "second"}

print(d)

# Operations allowed on frozenset
# Even though it is immutable, set operations still work.

a = frozenset([1,2,3])
b = frozenset([3,4,5])

print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference : -> it removes common elements and returns elements in a

#  way 1 Frozenset(iterable)

f = frozenset(int(input("Enter: ")) for i in range(4))
print(f)

#  way 2 Frozenset
temp = []   # temporary list

for i in range(4):
    n1 = int(input("Enter n1: "))
    temp.append(n1)

f = frozenset(temp)
print(f"frozenset is {f}")
