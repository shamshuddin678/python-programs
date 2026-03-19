l = [9,89,79,69]

# index = 0
# for i in l:
#     index += 1
#     print(f"In list at is {index} and value {i}")
# instead of above using that we use this below one enumerate()
for index,item in enumerate(l):
    print(f"In list at is {index} and value {item}")