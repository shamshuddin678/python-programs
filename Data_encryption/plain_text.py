cipher = input("Enter cipher text: ")
key = int(input("Enter key: "))

plain = ""
for i in cipher:
    ordvalue = ord(i)
    plain_value = ordvalue - key
    plain += chr(plain_value)

print(plain)

'''
DRY RUN:
->Step 1
i = 'j'
ord('j') = 106
106 - 2 = 104
chr(104) = h
plain = "h"

->Step 2
i = 'g'
ord('g') = 103
103 - 2 = 101
chr(101) = e
plain = "he"

->Step 3
i = 'n'
ord('n') = 110
110 - 2 = 108
chr(108) = l
plain = "hel"

->Step 4
i = 'n'
ord('n') = 110
110 - 2 = 108
chr(108) = l
plain = "hell"

->Step 5
i = 'q'
ord('q') = 113
113 - 2 = 111
chr(111) = o
plain = "hello"

->Step 6
i = '#'
ord('#') = 35
35 - 2 = 33
chr(33) = !
plain = "hello!"

->Step 7
i = '*'
ord('*') = 42
42 - 2 = 40
chr(40) = (
plain = "hello!("

->Step 8
i = '%'
ord('%') = 37
37 - 2 = 35
chr(35) = #
plain = "hello!(#"
'''