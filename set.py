#sets are unordered items(A Set does not maintain any order of elements)
#sets are unique items(A Set does not allow duplicate elements )
my_set = {10,20,30,33,40,0,0,0}
my_set.add(50) #adding an element to the set
my_set.add(55) #adding an element to the set
#my_set.sort() #sets do not support sorting
print(my_set)

#sets supports updating with multiple elements
my_set.update([60,70,80])
print("my_set after update:",my_set)

# sets operations
# 1.union()
print("Union: ",my_set.union({2005,2006})) #it adds the elements to the set

# 2.intersection()
print("Intersection: ",my_set.intersection({0,2005,2006}))

# 3.difference() : “remove common items”
print("Difference: ",my_set.difference({0,2005,2006}))

# 4.symmetric_difference() : “keep only non-common items”
print("Symmetric difference: ",my_set.symmetric_difference({0,2005,2006}))
