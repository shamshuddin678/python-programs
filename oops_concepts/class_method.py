class method:
    a = 1

    @classmethod  # decorator is used to create a class method.
    # if we want the class attribute use cls
    def show(cls):
        print(f"The class attribute is {cls.a}")

m = method()
# print(m.a) # class attribute is not changed

m.a = 23
# print(m.a) # it shows instance attribute but i want to class attribute

m.show()