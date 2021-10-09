n = int(input())        #Nhập số phần tử của mảng
a = list(map(int,input().split()))      #Nhập các phần tử của mảng
k,x = list(map(int,input().split()))    #Nhập giá trị k và x (0 < k <= n)
list = []       #Tạo 1 list rỗng
a.sort()        #Sắp xếp list a theo thứ tự tăng dần
for i in a:     #Chạy vòng lặp list a
    list.append((abs(x-i),i))       #Sau mỗi vòng sẽ thêm 1 list con gồm 2 phần tử vào list mẹ
list.sort()     #Sắp xếp list mẹ theo thứ tự tăng dần
kq = []         #Tạo 1 list kết quả
for i in range(0,k):        #Chạy vòng lặp (i chạy từ 0 đến k - 1)
    kq.append(list[i][1])       #Sau mỗi vòng lặp sẽ lấy phần tử thứ 2 của list con ở phần tử thứ i của list mẹ và thêm vào list kết quả
kq.sort()       #Sắp xếp list kết quả theo thứ tự tăng dần
for i in kq:
    print(i,end ='  ')      #In các giá trị trong list kết quả ra màn hình