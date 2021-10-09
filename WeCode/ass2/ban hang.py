q = int(input())        #Nhập số testcase
a = []      #Tạo 1 list a để đưa ra giá bán đồng giá tối thiểu    

while q > 0:    
    n = int(input())    #Nhập số sản phẩm
    b = []      #Tạo 1 list để nhập giá gốc của các sản phẩm
    b = list(map(int,input().split()))[:n]     #Nhập giá gốc của n sản phẩm
    if (sum(b) % n == 0):       #Tìm giá bán đồng giá tối thiểu cho từng sản phẩm
        a.append(int(sum(b) / n))    #Thêm giá bán vừa tìm được vào list a
    else:
        a.append(int(sum(b) // n + 1))
    q -= 1      #Giảm 1 testcase sau mỗi lần chạy vòng while
for i in a:
    print(i)        #In giá bán đồng giá tối thiểu ra màn hình