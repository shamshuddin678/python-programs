# Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)
s.add("18")
print(s) # it prints output: {18,'18'} it means 18=integer and '18'=string 