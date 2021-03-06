from random import random, seed
from RingProduct import Ring

def cal_avg_area(n=10, seed_value=5):
    seed(seed_value)
    rings = [Ring(radius=random()*10) for i in range(n)]

    total = 0

    for r in rings:
        total += r.area()
        print("Ring radius :{}, area :{}, total :{}".format(r.radius, r.area(), total))
    avg_area = sum([total])/n
    return avg_area

def expansion(radius = 1.0, expansion=2.0):
    radius *= expansion
    return radius

def main():
    # n=10
    # avg_area = cal_avg_area(n=10)
    # print("Avg area for n = {0} is :{1:.2f}".format(n,avg_area))
    radii = [2,4,7]
    rings = [Ring(radius=r) for r in radii]
    for r in rings:
        print("Radius :{}".format(r.radius))
        print("Perimeter at room temp {:.2f}".format(r.perimeter()))
        r.radius = expansion(r.radius)
        print("Perimeter at heating {:.2f}".format(r.perimeter()))

if __name__ == '__main__':
    main()

