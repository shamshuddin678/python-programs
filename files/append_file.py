# append file. it addeds at last

str = "I have perfectly appended the string in the file file.txt"

f = open("files/file.txt","a")

f.write(str)
f.close()