q = int(input())
for i in range (q):
    n,k = list(map(int,input().split()))
    a = [int(i) for i in input().split()]
    b = a.count(k)
    print(b)