def area(height,b1,b2):
    ar = (b1+b2) / 2 * height
    return ar

height = float(input())
b1 = float(input())
b2= float(input())
res = area(height,b1,b2)
print(res)