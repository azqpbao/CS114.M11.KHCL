from bisect import bisect_left
from sys import stdin

n = int(input())
arr = [int(i) for i in stdin.readline().split()]

def Index_closeX(arr,x):
    return bisect_left(arr,x)

def Print_a_closeX(arr,a,x):
    arr_1 = []
    index = Index_closeX(arr,x)
    if index == 0:
        return arr[0:a]
    elif index == len(arr) - 1 or index == len(arr):
        return arr[len(arr)-a:len(arr)]
    else:
        left = index
        right = index + 1
        if x - arr[left] <= arr[right] - x:
            arr_1.append(arr[left])
            left -= 1
        else:
            arr_1.append(arr[right])
            right += 1
        a -= 1
    while a != 0:
        if left < 0 and right < len(arr) - 1:
            arr_1.append(arr[right])
            right += 1
        elif left >= 0 and right > len(arr) - 1:
            arr_1.append(arr[left])
            left -= 1
        else:
            if x - arr[left] <= arr[right] - x:
                arr_1.append(arr[left])
                left -= 1
            else:
                arr_1.append(arr[right])
                right += 1
        a -= 1
    arr_1.sort()
    return arr_1

while True:
    b = [int(i) for i in stdin.readline().split()]
    if len(b) == 0:
        break
    else:
        ans = Print_a_closeX(arr,b[0],b[1])
        print(ans[0], ans[-1])