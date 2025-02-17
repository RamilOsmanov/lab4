def sq(n):
    for i in range (n+1):
        yield i**2


n = int(input())
for res in sq(n):
    print(res)