q = int(input())    #Nhập số lượng testcase
for k in range (q):     #Tương ứng với từng testcase, nhập các chuỗi
  s = input()   #Nhập chuỗi s 
  t = input()   #Nhập chuỗi t
  n = 0     #Gán n = 0
  for i in s:   #Dò các chữ cái trong chuỗi s
    if n == 0:  
      for j in t:   #Nếu n = 0 thì dò các chữ cái trong chuỗi t
        if i == j:    #Kiểm tra xem có chữ cái nào trong chuỗi s trùng với chữ cái trong chuỗi t không
          n += 1      #Nếu có thì n = 1
          break       #Sau đó dừng vòng lặp dò chữ cái trong chuỗi t
    else:             
      break           #Nếu n = 1 thì dừng vòng lặp dò chữ cái trong chuỗi s

  if (n == 1) & (len(s) == len(t)):   #Kiểm tra xem có chữ cái nào trùng nhau trong 2 chuỗi và 2 chuỗi có số chữ cái = nhau hay ko
    print('YES')      #Nếu có thì in YES
  else:
    print('NO')       #Ngược lại in NO