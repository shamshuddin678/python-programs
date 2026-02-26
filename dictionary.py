# Dictionaries are key : value pairs
'''properties of Dictionaries are
1.It is unordered
2.It is a mutable
3.It is indexed
4.Cannot contain duplicate keys'''

l = {"1sem1": "c language",
"1sem2": "Data strucures",
"2sem1": "oops through java",
"2sem2": "python"
}
print(l["2sem2"])
print((l["2sem1"]))

# dictionary methods
# 1.items() = it returns all the key: value pairs of a dictionary as tuples
# for k,v in l.items():
    # print(k,":",v) in this can also we print 
print(l.items())

# 2.keys() =it returns all the keys of a dictionary
print(l.keys())

# 3. update() the key:value pairs in dictionary
l.update({"lovable language": "python"}) # update returns none so ❌ don't print it

# 4. pop() it Removes a specific key: value from the dictionary 
print(l.pop("lovable language"))

# 5.clear() it Removes all items from the dictionary
l.clear() # clear returns none so ❌ don't print it