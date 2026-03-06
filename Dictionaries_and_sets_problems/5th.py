# Way 1
d={}

name=input("Enter friends: ")
language=input("Enter language: ")
d.update({name:language})

name=input("Enter friends: ")
language=input("Enter language: ")
d.update({name:language})

name=input("Enter friends: ")
language=input("Enter language: ")
d.update({name:language})

name=input("Enter friends: ")
language=input("Enter language: ")
d.update({name:language})

name=input("Enter friends: ")
language=input("Enter language: ")
d.update({name:language})

print(d)

# way 2
n = int(input("Enter : "))
dict = {}

for i in range(1,n+1):
    name = input("Enter name: ")
    language = input("Enter language: ")
    dict.update({name : language})

print(dict)    