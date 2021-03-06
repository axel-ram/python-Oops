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

def main ():
    print("Center of ring is : {}".format(Ring.center))
    r = Ring(price = 40000)
    print("Ring radius :{}, area :{}, Cost :{}".format(r.radius, round(r.area(),2), r.cost()))
    columns = ['radius', 'date', 'metal']
    for col in columns:
        print('{} : {}'.format(col, getattr(r,col)))

if __name__ == '__main__':
    main()

