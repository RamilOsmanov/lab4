def cou(n):
    while n > 0:
        yield n - 1
        n -= 1

n = int(input())
for res in cou(n):
    print(res)
