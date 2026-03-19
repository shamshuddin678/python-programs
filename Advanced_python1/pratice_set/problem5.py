'''
Store the multiplication tables generated in problem 3 in a 
file named Tables.txt
'''
n = int(input("Enter n: "))

table = [n * i for i in range(1,11)]
with open("Advanced_python1/pratice_set/Tables.txt","a") as f:
    f.write(f"Table {n}: {str(table)} \n")