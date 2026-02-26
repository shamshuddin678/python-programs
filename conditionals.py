#leap year checking
year=int(input("Enter a year: "))

if(year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print(f"you entered {year} is a leap year")
else:
    print(f"you entered {year} is not a leap year")
print()
print("-----")

# finding momentum
mass=float(input("Enter the mass: "))
velocity=float(input("Enter the velocity: "))
print(f"The momentum is: {mass * velocity} kg m/s") 