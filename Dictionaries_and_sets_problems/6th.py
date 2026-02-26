# 1.If the names of 2 friends are same; what will happen to the program in problem 6?
# . If languages of two friends are same; what will happen to the program in problem 6?
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
print(d)

'''
Note:- 1.If the names of 2 friends are same ,then it updates a language
2.If the languages are same of 2 friends then it returns a same language
'''