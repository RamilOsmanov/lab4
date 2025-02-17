import math
def are(n,l):
    area = (n * l**2) / (4 * math.tan(math.pi / n))
    return area

n= int(input())
l = float(input())
res = are(n,l)
print (res)