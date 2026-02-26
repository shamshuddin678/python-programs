a1 = int(input("Enter 1st subject marks: "))
a2 = int(input("Enter 2nd subject marks: "))
a3 = int(input("Enter 3rd subject marks: "))

# Calculate total percentage
total_percentage = (a1 + a2 + a3) / 300 * 100

# Check conditions
if(total_percentage>=40 and a1>=33 and a2>=33 and a3>=33):
    print("You are passed")

else: # marks and total_percentage are < 
    print("You are failed try better for next time. GOOD TRY")

print("Your total percentage is:", total_percentage)
