class Car:
    def __init__(self,acc,brk,clutch):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True      
        self.clutch = True
        print(f"The car is started") 

c = Car(34,12,3)
c.start()          