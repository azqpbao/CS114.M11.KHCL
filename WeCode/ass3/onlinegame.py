server = set()      #Tạo 1 danh sách chứa dữ liệu người chơi theo kiểu dữ liệu set để tránh bị trùng lặp
while 1:
    l = [int(i) for i in input().split()]       #Nhập input
    if l[0] == 1:       #Kiểm tra xem số thứ nhất có phải là 1 không
        server.add(l[1])        #Nếu đúng thì thêm dữ liệu người chơi (là số thứ 2) vào danh sách server
    elif l[0] == 2:     #Kiểm tra xem số thứ nhất có phải là 2 không
        print(int(l[1] in server))      #Nếu đúng thì kiểm tra xem dữ liệu người chơi (là số thứ 2) có trong danh sách server không và nén thành kiểu int. Nếu có thì xuất 1, không thì xuất 0
    elif l[0] == 0:     #Nhập số 0 để kết thúc chương trình
        break