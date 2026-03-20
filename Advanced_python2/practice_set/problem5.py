from functools import reduce 
def greater(a,b):
    if(a > b):
        return a
    return b

n = [1,25,35,545,654,355,365,75,67,343,]
print(reduce(greater,n))