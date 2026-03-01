from random import randint
class Train:

    def __init__(slf,trainNo):
        slf.trainNo = trainNo


    def tickets_booking(self,fro,to):
        print(f"Your ticket is booked in the trainNo: {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"TrainNo is {self.trainNo} is running on time")

    def get_fare(self,fro,to):
        print(f"Ticket fare in trainNo: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(240516)
t.tickets_booking("vijayawada","hyderabad")
t.get_status()
t.get_fare("vijayawada","hyderabad")