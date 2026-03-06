'''Write a program to input eight numbers from the user and display all the unique
numbers (once).'''
# way 1
s=set()
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
a=input("Enter value: ")
s.add(int(a))
print(s) #printing all sets elements
print(len(s))

# way 2
s = set()
for i in range(1,9):
    n = int(input("Enter n: "))
    s.add(n)

print(s)    