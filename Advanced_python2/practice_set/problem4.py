def divisible5(n):
    if(n %5 == 0):
        return True
    return False
n = [1,25,35,545,355,365,75,67,343,]
onlydivsible = list(filter(divisible5,n))
print(onlydivsible)