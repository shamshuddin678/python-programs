class Men:
     def __init__(self,name,work_place,code): # Here we used self parameter
          self.name = name
          self.work_place = work_place
          self.code = code
          print(f"The men name is {self.name}, working at {self.work_place} and code in {self.code} language")

          @staticmethod # If we use the @staticmethod we no need to use the self parameter
          def display():
               print("Method is showing without using self parameter")

m = Men("shamshuddin","Sharjah","python")
