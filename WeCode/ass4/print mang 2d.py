r, c = list(map(int, input().split()))		#Nhập số dòng r và số cột c của mangr
a = [[]] * r		#Tạo 1 list mẹ a gồm r list con
Length = [0] * c	 #Tạo 1 list Length gồm c phần tử = 0
for i in range (r):		
	a[i] = [int(x) for x in input().split()]	#Ứng với mỗi list con trong a nhập c phần tử
	for j in range (c):		
		Length[j] = max(Length[j],len(str(a[i][j])))		#Tìm độ rộng lớn nhất của các phần tử ứng với các vị trí trong list con của list a
kq = ""		#Tạo 1 mảng kq
b = 0		#Tạo 1 biến b = 0
ans = ''	#Tạo 1 chuỗi ans
for i in a:		#Duyệt list a
	d = 0		#Tạo 1 biến d = 0
	for j in i:		#Duyệt các phần tử trong list con của a
		#Lúc này đã biết độ rộng của từng cột trong mảng (đc lưu trong list Length)
		ans = str(j).rjust(Length[d], " ")		#Các phần tử được căn lề phải với độ rộng tương ứng trong list Length được lưu vào chuỗi ans
		kq = kq + ans 		#Gán từng phần tử trong chuỗi ans vào mảng kq
		if d < c - 1:		#Kiểm tra xem số phần tử của từng hàng nhỏ hơn số cột c không
			kq = kq + " "	#Nếu nhỏ hơn thì in khoảng trắng và tiếp tục in phần tử tiếp theo
		else: 				
			kq = kq + "\n"	#Nếu bằng thì xuống hàng và tiếp tục in phần tử tiếp theo
		d += 1
	b += 1
print(kq)		#Sau khi đã in hết phần tử vào mảng kq thì xuất kq ra màn hình