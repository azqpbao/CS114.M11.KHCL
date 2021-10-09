n,m = list(map(int,input().split()))        #Nhập n hàng và m cột ma trận thứ 1
r,c = list(map(int,input().split()))        #Nhập r hàng và c cột ma trận thứ 2
l = []      #Tạo 1 list rỗng

if m * n != r * c:      #Kiểm tra xem có thể reshape ma trận không 
    for i in range (n):    
        a = input()     #Nếu không thì nhập các phần tử của ma trận thứ 1 rồi xuất ra ngoài màn hình
        print(a)
else:       #Có thể reshape
    for i in range (n):     
        a = input()     #Nhập các phần tử của ma trận thứ 1
        l += a.split(' ')       #Thêm các phần tử ma trận thứ 1 vào list rỗng l
        if len(l) > c:      #Kiểm tra xem số phầm tử của ma trận thứ 1 có lớn hơn số cột của ma trận thứ 2 không
            print(*l[:c])       #Nếu có thì lần lượt xuất c phần tử của list l ra màn hình
            l = l[c:]       #list l sẽ xóa đi c phần tử đã được xuất để tránh bị trùng lặp
print(*l[0:c])      #Xuất c phần tử cuối cùng ra màn hình do vòng lặp trên sẽ dừng trước khi xuất c phần tử cuối ra ngoài