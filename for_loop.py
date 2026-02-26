# In for loop we use range function range(start,stop,step_size)
for i in range(1,11):
    print(i)

# list using for() loop
l=[1,2,"shamshuddin","Hello"]
for i in l:
    print(i)

# tuple using for() loop
t=("APPLE","BANANA","ORANGE",)
for i in t:
    print(i)

# string using for() loop
s='shamshuddin'
for i in s:
    print(i)

# NOTE:- for() loop wih else
'''
Important points
1.else executes only when the for loop finishes normally
2.If the loop is not stopped by a break, the else block runs
3.No more items in the list->Loop exhausted normally->So the else block runs
4.The else in a for-loop runs only when:
->The loop does not break
->The loop ends normally and else executes
5.If we used a break, the else wouldn't execute.
'''    