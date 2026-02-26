# break statement
for i in range(1,40):
     if(i==11):
         break # it exits and prints the value of i
print(i)

'''
LOOP explaination:
->Loops from 1 to 10
->When i becomes 11, the loop breaks
->So printing stops at 10
->break, it jumps out of the loop completely, even if there are more iterations left.
'''

# continue statement 
for i in range(1,60):
    if(i==31):
        continue # means in this loop upto iteration skips and continue 
    print(i)
#output:
''' 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30(here it skips 31 and continue 32 to 60)
32
33
34
35
36
37
'''    