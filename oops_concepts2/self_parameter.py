class Men:
     def __init__(self,name,work_place,code): # Here we used self parameter
          self.name = name
          self.work_place = work_place
          self.code = code
          print(f"The men name is {self.name}, working at {self.work_place} and code in {self.code} language")

m = Men("shamshuddin","Sharjah","python")
