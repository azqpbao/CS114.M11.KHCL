n = int(input())
def Sum(n):
    a = []              #Tạo 1 list 
    k = 0               #Khởi tạo giá trị ban đầu để tính tổng các ước số
    for i in range (1,n):
        if n % i == 0:  #Tìm ước số
            a.append(i) #Thêm ước số vừa tìm được vào list a đã khởi tạo
    for j in a:         #Lấy các ước số trong list a ra
        k = k + j       #Cộng các ước số lại với nhau   
    return k            #Trả về giá trị tổng các ước số sau khi cộng xong
print(Sum(n))           #Xuất kết quả