def average(*nums):
    sum=0
    print(type(nums))
    for i in range(len(nums)):
        sum=sum+nums[i]
        print("Average is: ", sum/len(nums))

average(1,2,3,4,5)        