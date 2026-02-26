# Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(c):
    f=(c * 9/5) + 32
    return f

f=int(input("Enter temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {c_to_f(f)} °F")


# Write a python program using function to convert Fahrenheit to Celsius.
def f_to_c(f):
    c=(f - 32) * 5/9
    return c

f=int(input("Enter temperature in Fahrenheit: "))
p=f_to_c
print(f"Temperature in Celsius: {round(p,2)} °C")
    