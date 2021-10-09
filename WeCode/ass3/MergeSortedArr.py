na,nb = map(int,input().split())    #Nhập số phần tử của từng chuỗi
a = list(map(int,input().split()))[:na]   #Nhập các phần tử của chuỗi a
b = list(map(int,input().split()))[:nb]   #Nhập các phần tử của chuỗi b
c = []    #Tạo 1 danh sách rỗng 
c = a + b   #Cộng 2 chuỗi a và b lại với nhau và bỏ vào trong list c
c.sort()    #Sắp xếp list c theo thứ tự tăng dần
print(*c)   #In ra các phần tử trong list c sau khi đã sắp xếp