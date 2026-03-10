def avg(*nums):
    sum=0
    print(type(nums))
    for i in range(len(nums)):
        sum=sum+nums[i]
    return sum/len(nums)

c=avg(1,2,3,4,5)
print(c)   