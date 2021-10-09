num = int(input())
n = len(str(num))       #Đổi biến num thành kiểu string để lấy số chữ số trong num (number of digits)
sum = 0         #Tạo biến sum để tính tổng lũy thừa
temp = num      #Tạo 1 biến temp bằng num
while temp > 0:     
    digit = temp % 10       #Lấy ra chữ số cuối cùng trong num. Vd: num = 123 thì lấy ra số 3
    sum += digit**n         #Nhân lũy thừa số digit vừa tìm được với n (number of digits)
    temp = temp // 10       #Bỏ số cuối cùng trong num đi và tiếp tục thực hiện vòng lặp while cho đến khi num hết sô 
if (sum == num):
    print("True")
else:
    print("False")