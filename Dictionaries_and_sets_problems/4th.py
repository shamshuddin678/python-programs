s=set()
s.add(20)
s.add(20.0) # Python compares only the VALUE, not the type 20=20.0 so, length=2
s.add("20")
print(s)
print(len(s)) # it prints output: s={20,'20'}

# Note: type of empty set 
s={}
print(type(s)) 