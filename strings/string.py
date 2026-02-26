my_string="Hello"
print(my_string)
# string slicing string[start:end(stop):step_size]
# ':' prints all the string 
print(my_string[:]) # -> it takes 0 to n-1 index( len(my_string)-1)
# string printing from last index to third last index
print(my_string[-1:-3])
# In string[start:stop:step] indexing printing 
print(my_string[::-3]) #→ move backward 3 steps.
'''
here H e l l o
    0 1 2 3 4
   -5-4-3-2-1
   [ : : -3] -> it starts from last index and moves backward 3 steps and prints the character
   here start with -1 to -3 with step -3
   so it prints o and then moves backward 3 steps and prints e
'''

#string printing from [firstindex:lastindex]
print(my_string[1:3])

# string index_start to index_end with step_size
# [ 0 : len(my_string) : 1 ]
print(my_string[ : : ])  