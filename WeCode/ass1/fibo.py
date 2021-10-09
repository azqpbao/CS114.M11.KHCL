x = int(input())        #Nhập số x

def fibonacci(x):
    f0 = 0              #Gán f(0) = 0
    f1 = 1              #Gán f(1) = 1
    fx = 1              #Gán f(x) = 1
    if (x < 1 or x > 30):       #Kiểm tra xem x có nằm trong khoảng [1,30] không
        return -1
    elif (x == 1):              #Nếu x = 1 thì xuất ra màn hình số fibonacci thứ x là 1
        return x
    else:
        for i in range (2,x):   #Vì x = 1 đã có kết quả nên sẽ chạy vòng lặp bắt đầu từ 2
            f0 = f1             #Gán f(0) = f(1)
            f1 = fx             #Gán f(1) = f(x)
            fx = f0 + f1        #Gán f(x) = f(0) + f(1)
        return fx
if (fibonacci(x) == -1):
    print("So",x,"khong nam trong khoang [1,30].")
else:
    print(fibonacci(x))