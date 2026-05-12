# way 1 .t = tuple(map(int,input("Enter elements: ).split()))
'''
example: 
"10 20 30"
        ↓
split()
        ↓
['10','20','30']
        ↓
map(int,...)
        ↓
[10,20,30]
        ↓
tuple()
        ↓
(10,20,30) '''

#tuple means if we use it . it cannot be changed
'''
->eval() : it evaluate & executes a python exprression that was wrritten in string.
-> eval() in integer : eval('10+20') . it converts string to int and displays
-> eval() in float : eval("3.14") . it converts string to float and displays
-> eval() in list : eval("[1,2,3]") . it converts string to list and displays
-> eval() in tuple : eval("(1,2,3)") . it converts string to tuple and displays
-> eval() in dictionary : eval("{'a':1,'b':2}") . it converts string to dictionary and displays
-> eval() in set : eval("{1,2,3,4}") . it converts string to set and displays
-> eval() in multiple elements : a,b = eval(input("Enter values: ")) . it converts string to multiple elements and displays
-> eval() in string operations: print(eval("'Hello' + ' Python'")) . it apply string operrations to set and displays

'''
my_tuple=eval(input("Enter my choice: "))

# tuple methods
print("Count: ",my_tuple.count(3)) # it counts occurrences of 3

print("Index: ",my_tuple.index(3)) #it returns the index of occurrence of 3

# tuple operations
'''1.concatenation
Tuples are immutable, so we cannot insert elements into them.
Instead, we can create a new tuple with the additional element.'''
new_tuple = my_tuple + (10,11,)
print("New tuple: ",new_tuple)

'''2.repetition
it can repeat the tuple elements'''
repeated_tuple=my_tuple*3
print("Repeated tuple: ",repeated_tuple)

'''3.membership
we can check if the element is present in the tuple or not using 'in' keyword'''
print("Membership: ",3 in my_tuple) #returns True
print("Membership: ",6 not in my_tuple) #returns True

# 4.length = Get the number of elements.
print("Length: ",len(my_tuple))
# 5.min & max = Get the smallest and largest elements.
print("Min: ",min(my_tuple))
print("Max: ",max(my_tuple))

# 6.slicing = Extract a portion of the tuple.(start:stop:step)
print(my_tuple[1:4])
