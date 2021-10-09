from sys import stdin
kq = []
while 1:
    a = [int(i) for i in stdin.readline().split()]
    if a[0] == 0:
        kq.insert(0,a[1])
    elif a[0] == 1:
        kq.append(a[1])
    elif a[0] == 2:
        if a[1] in kq:
            kq.insert(kq.index(a[1]) + 1,a[2])
        else:
            kq.insert(0,a[2])
    elif a[0] == 3:
        if a[1] in kq:
            kq.remove(a[1])
    elif a[0] == 4:
        while a[1] in kq:
            kq.remove(a[1])
    elif a[0] == 5:
        if kq:
            kq.pop(0)
    elif a[0] == 6:
        break
if len(kq) == 0:
    print('blank')
else:
    for i in kq:
        print(i,end = ' ')