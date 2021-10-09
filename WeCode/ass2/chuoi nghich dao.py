a = str(input())
b = str(input())

if b[::-1] == a:        #Kiểm tra b có phải là chuỗi đảo ngược của a không
    print('YES')
else:
    print('NO')