#string slicing 
s1 = "shamshuddin"

"""
string slicing :
-> string[staring_index : ending_index] . means it will prints start to end ignores ending_index
-> string[starting_index :] .means go till end of the string
-> string[ : ending_index]. means default it take 0 as starting index to ending_index. ignores ending_index
-> string[ : ] . means it will take whole string to print
-> string[startimng_index : ending_index : step_size] . means it will print the string start to end with that parallel step_size is incrementing or decrementing
"""

print(s1[0:10]) # it will print from index 0 to index 9 ignores 10th index
print(s1[0 : ]) # it will print from index 0 to end of the string
print(s1[ : 10]) 
print(s1[ : ]) # it will print whole string
print(s1[0 : 10 : 2]) # it will print from index 0 to index 10 with step size of 2
print("----- ends string slicing -----")
# string negative slicing
"""
string negative slicing:
-> string[-starting_index : -ending_index] . means it will print from end of the string to start of the string with negative indexing
example: "s h a m s h u d d i n"
index:    0 1 2 3 4 5 6 7 8 9 10
negative_index: -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
                 s   h   a  m  s  h  u  d  d  i  n
->string[-starting_index : ] . means it will print from starting at particular index increases the negative indexing(ex: s1[-3 : ](from -3 to -1),start neagtive index to end of the negative index)
->string[ : -ending_index] . means it will takes from beginning of the string to the negative index(ex: s1[ : -3], start from 0 to -3 index)
->string[ : : -step_size] . means it will print the string in reverse order with step size of negative step size(ex: s1[ : : -1], it will takes 1st : -1, then -2, then -3 and so on)
->string[-starting_index : -ending_index : -step_size]. means it will take -starting_index to -ending_index with step_size of negative step size
"""
print("----- starts negative slicing -----")
# print(s1[-1 : -8]) # python automatically takes from negative onwards no need to intialize the start_index in negative slicing  
print(s1[-8 : ]) # it take to print from -8 to -1
print(s1[  : -8]) # it will take to print from -11 to -8
print(s1[ :  : -1])
print(s1[-1 : -9 : -1])


