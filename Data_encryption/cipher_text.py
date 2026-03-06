plain = input("Enter plain text: ")
key = int(input("Enter key: "))

cipher = ""
for i in plain:
    ordvalue = ord(i)
    cipher_value = ordvalue + key
    cipher += chr(cipher_value)

print(cipher)
'''
DRY RUN:
->Step 1
i = 'h'
ord('h') = 104
104 + 2 = 106
chr(106) = j
cipher = "j"

->Step 2
i = 'e'
ord('e') = 101
101 + 2 = 103
chr(103) = g
cipher = "jg"

->Step 3
i = 'l'
ord('l') = 108
108 + 2 = 110
chr(110) = n
cipher = "jgn"

->Step 4
i = 'l'
ord('l') = 108
108 + 2 = 110
chr(110) = n
cipher = "jgnn"
->Step 5
i = 'o'
ord('o') = 111
111 + 2 = 113
chr(113) = q
cipher = "jgnnq"

->Step 6
i = '!'
ord('!') = 33
33 + 2 = 35
chr(35) = #
cipher = "jgnnq#"

->Step 7
i = '('
ord('(') = 40
40 + 2 = 42
chr(42) = *
cipher = "jgnnq#*"

->Step 8
i = '#'
ord('#') = 35
35 + 2 = 37
chr(37) = %
cipher = "jgnnq#*
'''