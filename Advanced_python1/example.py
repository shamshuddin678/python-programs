class Time:
    def __init__(self,hour,min,sec):
        self.hour = hour
        self.min = min
        self.sec = sec
    def __add__(self,other):
        hour = self.hour + other.hour 
        min = self.min + other.min
        sec = self.sec + other.sec

        min_add,sec = divmod(sec,60) # (a // b,a % b)
        min_add += min_add
        hour_add,min = divmod(min,60)
        hour_add += hour_add
        return f"{hour}hr : {min}min : {sec}sec"       

t1 = Time(2,20,20)       
t2 = Time(2,50,60)
print(f"the 2 time objects added are {t1 + t2}")
