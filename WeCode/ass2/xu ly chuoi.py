a = str(input()).lower()        #Nhập 1 chuỗi bất kì với hàm lower để chuyển hết sang chữ thường
b = ['A','O','Y','E','U','I','a','o','y','e','u','i']       #Tạo 1 list với các nguyên âm cần xóa
c = ''      #Tạo 1 string rỗng

for i in a:
    if i in b:      #Kiểm tra xem có nguyên âm trong chuỗi a không
        a = a.replace(i,'')     #Nếu có thì xóa đi
for i in a:
    c = c + '.'     #Thêm dấu chấm vào chuỗi c
    c = c + i       #Sau khi thêm dấu chấm thì bỏ từng phụ âm trong chuỗi a vào chuỗi c và lặp lại
print(c)            #In chuỗi c kết quả ra màn hình