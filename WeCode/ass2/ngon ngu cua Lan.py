a = list(map(str,input().split()))      #Nhập chuỗi
b = [0]*len(a)      #Tạo 1 list b có số phần tử 0 bằng với số từ trong chuỗi a
str = ["lios","liala","etr","etra","initis","inites"]   #Tạo 1 list gồm các từ Lan's language (sắp xếp theo đúng thứ tự DT + ĐT + TT và giới tính nam nữ xen kẽ)

if len(a) == 1:     #Kiểm tra xem chuỗi a chỉ có 1 từ hay không
    for i in range(6):      
        if a[0].endswith(str[i]):   #Nếu đúng thì kiểm tra xem từ đó có thỏa đk Lan's language không
            print("YES")        #Nếu đúng thì in YES
            exit(0)     #Thoát khỏi chương trình

    print("NO")     #Nếu sai thì in NO
    exit(0)     #Thoát khỏi chương trình

for i in range(len(a)):     #Chạy vòng lặp chuỗi a
    for j in range(6):      #Chạy vòng lặp danh sách các từ trong str
        if a[i].endswith(str[j]):       #Kiểm tra từng từ trong chuỗi a xem tận cùng có phải là các từ trong danh sách str không
            b[i] = j + 1        #Nếu có thì phần tử thứ i trong danh sách b sẽ bằng j + 1
            break       #Thoát khỏi vòng lặp j
    if b[i] == 0:       #Kiểm tra xem có tồn tại từ nào trong chuỗi a tận cùng là các từ trong danh sách str không
        print("NO")     #Nếu không thì in NO 
        exit(0)     #Thoát khỏi chương trình
#Sau khi các từ trong chuỗi a đều tận cùng là các từ trong danh sách str thì bắt đầu kt thứ tự và giới tính của các từ trong chuỗi a
gay = b[0] % 2      #Đặt 1 biến gay = phần dư của phần tử đầu tiên của danh sách b chia cho 2
for i in range (len(b)):        #Chạy vòng lặp danh sách b
    if (b[i] % 2) != gay:       #kiểm tra xem các từ trong chuỗi a có cùng giới tính không
        print('NO')     #Nếu không thì in NO
        exit(0)     #Kết thúc chương trình
x = sorted(b)       #Sắp xếp lại danh sách b để kiểm tra thứ tự từ 
cnt = 0     #Đặt 1 biến cnt = 0

for i in range(len(b)):        #Chạy vòng lặp danh sách b
    if b[i] == 3 or b[i] == 4:      #Kiểm tra xem có tồn tại danh từ trong chuỗi a không
        cnt += 1       #Nếu có thì thì cnt cộng thêm 1
    if b[i] != x[i]:    #Kiểm tra xem thứ tự đã sắp xếp đúng theo chuẩn Lan's language chưa
        print("NO")     #Nếu sai thì in NO
        exit(0)     #Thoát khỏi chương trình
#Kiểm tra số danh từ có trong chuỗi 
if cnt == 1:        #Nếu chỉ có 1 danh từ trong chuỗi
    print("YES")        #In YES
else:       #Nếu không có danh từ nào hoặc có nhiều hơn 1 danh từ 
    print("NO")     #In NO