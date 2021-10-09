n = int(input())        #Nhập số lượng phân số

import math     #Import thư viện math
for i in range (n):     
    a,b = map(int,input().split())      #Nhập tử số và mẫu số
    c = math.gcd(a,b)       #Tìm ước chung lớn nhất của tử và mẫu rồi gán vào biến c
    if b < 1:      #Kiểm tra xem mẫu số có bé hơn 1 không
        print(a)        #Nếu có thì chỉ xuất ra tử số
    else:
        if a % b == 0:      #Nếu tử số chia hết cho mẫu số
            print(a // b)       #In ra kết quả thương của tử và mẫu
        else:
            print(a // c,b // c)    #Nếu không chia hết thì chia cả tử và mẫu với ước chung lớn nhất (nếu có)