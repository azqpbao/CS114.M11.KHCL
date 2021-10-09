from sys import stdin
n,m = map(int,stdin.readline().split())
arr = []

for i in range (n):
    a = list(map(int,input().split()))[:m]
    arr.append(a)

t,l,b,r=map(int,input().split())
x = [0] * m
trai = [0] * l
phai = [0] * (m - r - 1)

for i in range(0,t):
    print(*x)

for i in range (t,b + 1):
    print(*(trai + arr[i][l:r + 1] + phai))

for i in range (b + 1,n):
    print(*x)