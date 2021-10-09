n,m = list(map(int,input().split()))
a = len(str(n))
if n > m % (10 ** a):
    print(m // 10**a)
else:
    print((m // 10**a) + 1)