k, t = map(int,input().split())
if (t // k) % 2 == 0:
    ga = t % k
else:
    ga = k - (t % k)
print(ga)