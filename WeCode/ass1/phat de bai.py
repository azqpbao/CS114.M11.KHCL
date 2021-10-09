n = int(input())
k = int(input())
p = int(input())
q = int(input())

a = (p - 1) * 2 + (q - 1) + k
b = (p - 1) * 2 + (q - 1) - k
if (b >= 0):
    print((b // 2) + 1,(b % 2) + 1)
elif (a <= n -1):
    print((a // 2) + 1,(a % 2) + 1)
else:
    print(-1)