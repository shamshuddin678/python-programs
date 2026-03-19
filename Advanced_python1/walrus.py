'''
Walrus operator: assign + use value in same line :=
instead os using this
l = len([1,2,3,4,5])
if(l > len(l)):
    n = len(l)
    print(n)
'''
if((n := len([1,2,3,4,5])) > 3):
    print(f"The list is too long {n} expected <= 3")