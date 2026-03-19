# Arbitary Arguments-> *args
def Arguments(*numbers):
    print(type(numbers)) # Here the <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Average is: ",sum / len(numbers))    

Arguments(5,6) # returns 5.5
Arguments(5,6,7,1)


# Arbitary Key Arguments- **kargs
def name(**name):
    # Here <class 'dict'>
    print(type(name))
    print("Hello,",name["mname"],name["lname"],name["fname"])

name(mname = "shamshuddin",lname = "raju",fname = "ganesh")