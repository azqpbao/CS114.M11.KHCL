<h1 align="center"><b>ĐỀ TÀI: NHẬN DẠNG CÁC LOẠI TRÁI CÂY</b></h>
<h1 align="center"><b>LỚP: CS114.M11.KHCL</b></h>

## Giảng viên:
1. Lê Đình Duy
2. Phạm Nguyễn Trường An
## Thành viên:
1. Lê Đình Đức - 19521372
2. Phan Anh Lộc - 19521766
3. Lưu Anh Dũng - 19521392
## 1. Ứng dụng:
  - Dùng để nhận diện 1 loại trái cây nào đó mà ta tình cờ bắt gặp và chưa từng thấy khi đi du lịch
## 2. Mô tả bài toán:
  - Input: Hình ảnh gồm 1 loại trái cây bất kì.
  - Output: 1 dòng text chưa tên của loại trái cây đó.
## 3. Mô tả về bộ dữ liệu:
  - Thu thập dữ liệu:
    - Dữ liệu là yếu tố quan trọng nhất và cũng là vấn đề mà chúng ta cần quan tâm nhất. Trong quá trình xây dựng một hệ thống phân loại trái cây, bước chuẩn bị và tiền xử lý dữ liệu quyết định tới thành bại của hệ thống hơn cả.
    - Với bài toán phân loại trái cây, dữ liệu ban đầu mình cần chuẩn bị là những hình ảnh được chụp bằng tay hoặc lấy từ trên mạng.
    - Bước tiếp theo, chúng ta sẽ tiến hành tiền xử lý dữ liệu trước khi đưa vào huấn luyện mô hình phân loại trái cây. Việc tiền xử lý dữ liệu là hết sức quan trọng để đảm bảo mô hình đạt được kết quả tốt
    - Gồm 40 loại trái cây, mỗi loại bao gồm 200 mẫu, được chia làm 2 tập train (X_train, y_train) và test (X_test, y_test) theo tỉ lệ 80% train, 20% test.


