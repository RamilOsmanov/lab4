def sq(n1,n2):
    for i in range (n1,n2+1):
        yield i**2


n1 = int(input())
n2 = int(input())
for res in sq(n1,n2):
    print(res)