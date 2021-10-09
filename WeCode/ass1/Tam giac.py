a = float(input())  #Nhập cạnh thứ 1
b = float(input())  #Nhập cạnh thứ 2
c = float(input())  #Nhập cạnh thứ 3

if (a + b > c) & (a + c > b) & (b + c > a) & (a > 0) & (b > 0) & (c > 0):   #Kiểm tra xem có phải là tam giác không
    import math             #Import thư viện math       
    CV = a + b + c          #Tinh chu vi tam giác                                                   
    p = CV/2                #Tinh nua chu vi tam giác
    DT = math.sqrt(p*(p-a)*(p-b)*(p-c))     #Tính diện tích tam giác
    if DT == int(DT):        #Kiểm tra xem diện tích có phải số nguyên không
        DT = int(DT)         #Nếu là số nguyên thì ép kiểu số nguyên cho diện tích, không bị ảnh hưởng bởi hàm round
    if (a == b) & (b == c):                 #Kiểm tra xem có phải tam giác đều không
        print("Tam giac deu, dien tich =",round(DT,2))
    elif (a == b) & (a != c) | (a == c) & (a != b) | (b == c) & (b != a):       #Kiểm tra xem có phải tam giác cân không
        print("Tam giac can, dien tich =",round(DT,2))
    elif (a * a == b * b + c * c) | (b * b == a * a + c * c) | (c * c == a * a + b * b):        #Kiểm tra xem có phải tam giác vuông không
        print("Tam giac vuong, dien tich =",round(DT,2))
    else:
        print("Tam giac thuong, dien tich =",round(DT,2))
else:
    print("Khong phai tam giac")