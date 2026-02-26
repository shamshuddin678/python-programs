#.split method by taking the input it converts the string into list of strings
# a=input("Enter the list of fruits: ").split()
a=input("Enter the list of fruits: ").split()
print(a)


# inserting element at specific index
a[0]="ORANGE"
print(a)

# string functions in lists
a.append("GRAPES") #append() means inserting at last 
a.insert(0,"MANGO")#insert() means inserting at some(index_number,value)
print(a)
# In lists using pop function
a.pop(3)
print(a)
#in lists we need to sort the elements use sort() function 
# And after sorting if we want to reverse it use sort(reverse=True)