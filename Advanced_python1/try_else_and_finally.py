try:
   a = int(input("Enter: "))
   print(a)
except Exception as e:
   print(e)
else:
   print("Try successfuly runned")

finally: # this runs both try and except sucessfuly runs 
   print("Iam running ")

# using function
def fun():
    try:
        a = int(input("Enter n: "))
        print(a)
    except Exception as e:
       print(e)
    
    finally:
      print("Iam on the way")
fun()    