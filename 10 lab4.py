import math
def fu(degree):
    radian = degree *math.pi / 180
    return radian



degree = float(input())
radian = fu(degree)
print(radian)
