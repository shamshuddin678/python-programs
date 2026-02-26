'''
search for a number x in this tuple given below using for loop
nums = (1,4,9,16,25,36,49,81,100)
''' 
nums = (1,4,9,16,25,36,49,81,100)
x = 36
for i in range(len(nums)):
    if(nums[i] == x):
        print(f"found at: {i}")
        break
else:
  print("not found")       