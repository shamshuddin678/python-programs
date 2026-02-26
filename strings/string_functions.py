# string functions

s1 = "i am a python programmer"
s2 = "24jr1a05bc"
s3 = "shamshuddin"
s4 = "12345"
print(s1.endswith("app")) # it returns false beacuse it ends with "mer" in my string
print(s1.startswith("I am")) #it prints true
print(s2.isalnum()) # checks alphabets and numbers
print(s3.isalpha()) # check aplhabets in string contains only connected letters ex: "shamshuddin".
print(s4.isdigit())
print(s3.islower())
s5 = "SHAMSHUDDIN"
print(s5.isupper())
print(s3.upper()) # it returns the uppre case letters 
print(s5.lower()) #it returns lower case letters
s6 = " "
print(s6.isspace()) #it returns true
s7 = " python "
print(s7.strip()) #it removes spaces are left & right
print(s7.lstrip()) #it removes spaces are left not right
print(s7.rstrip()) #it removes spaces are right not left
print(s3.replace("sham","SHAM")) # it replaces the replace(old_string,new_string)
s = "apples,bananas,dates"
print(s.split(",")) # split method : it converts the string into list

list = ["My","primary","language","is","python"] # join list to string
print(" ".join(list))  # " " is for to print the string after join the list
print(s1.capitalize()) # it takes only sentence of 1st letter "i" -> "I"
print(s1.find("i")) # it finds the position of the that letter
print(s1.count("i")) # it returns how many times is present in the give string
