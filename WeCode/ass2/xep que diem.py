q = int(input())
for i in range (q):
    n = int(input())    #Nhập số diêm tương ứng với từng testcase
    if n == 2:      
        print('2')      #Nếu số diêm = 2 thì thêm 2 que
    elif n % 2 == 0:
        print('0')      #Nếu số diêm khác 2 và chia hết cho 2 thì ko thêm que nào
    else:
        print('1')      #Nếu số diêm không chia hết cho 2 thì thêm 1 que