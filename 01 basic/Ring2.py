import math
import time
from datetime import datetime
class Ring (object):
    date = time.strftime("%Y-%m-%d", time.gmtime())
    center = 0.0
    def __init__(self, date = "06-03-2021", metal = 'Platinum', radius=5, price=35000, quantity=10):
        self.date = datetime.strptime(date, "%m-%d-%Y")
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity
    def cost(self):
        return self.price * self.quantity
    def area(self):
        return math.pi*self.radius**2

r1 = Ring()
print("Ring metal :{}, date :{}".format(r1.metal, r1.date))
print("Ring area :{}, Cost :{}".format(round(r1.area(),2), r1.cost()))
print(Ring.date)
r1.radius = 7
r1.price = 42000
r1.quantity = 8


print("Ring metal :{}, date :{}".format(r1.metal, r1.date))
print("Ring area :{}, Cost :{}".format(round(r1.area(),2), r1.cost()))
print(Ring.date)