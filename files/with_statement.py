f = open("files/file.txt")
f.read()
print(f)
f.close()

'''
Instead of this file closing we use the with statement.
with statement is automatically opens and closes the file.
'''
with open("files/file.txt") as f:
    print(f.read())

quote = "ok. learn and update as advance developer"
with open("files/file.txt","w") as f:
    f.write(quote)
        