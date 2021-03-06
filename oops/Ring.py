import math
import time
class Ring (object):
    date = time.strftime("%Y-%m-%d", time.gmtime())
    center = 0.0
    def __init__(self, date, metal, radius, price, quantity):
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity
    def cost(self):
        return self.price * self.quantity
    def area(self):
        return math.pi*self.radius**2

r1 = Ring("2021-03-05", 'Gold', 4, 12000, 2)
print("Ring metal :{}, date :{}".format(r1.metal, r1.date))
print("Ring area :{}, Cost :{}".format(round(r1.area(),2), r1.cost()))
print(Ring.date)