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
  - Dùng để nhận diện 1 đoạn văn được viết bằng tay bằng tiếng việt và chuyển đoạn văn đó sang dạng text trên máy tính
## 2. Mô tả bài toán:

- Input: Hình ảnh gồm 1 ký tự viết tay tiếng Việt.
- Output: Hình ảnh chữ cái tương ứng với input.

![](Image/input_output.png)

## 3. Mô tả về bộ dữ liệu:
  - Thu thập dữ liệu:
    - Dữ liệu là yếu tố quan trọng nhất và cũng là vấn đề mà chúng ta cần quan tâm nhất. Trong quá trình xây dựng một hệ thống phân loại chữ viết tay, bước chuẩn bị và tiền xử lý dữ liệu quyết định tới thành bại của hệ thống hơn cả.
    - Với bài toán phân loại chữ viết tay bằng tiếng việt, dữ liệu ban đầu mình cần chuẩn bị là những hình ảnh được viết bằng tay.
    - Bước tiếp theo, chúng ta sẽ tiến hành tiền xử lý dữ liệu trước khi đưa vào huấn luyện mô hình phân loại chữ viết tay. Việc tiền xử lý dữ liệu là hết sức quan trọng để đảm bảo mô hình đạt được kết quả tốt
    - Chia làm 2 tập train (X_train, y_train) và test (X_test, y_test) theo tỉ lệ 80% train, 20% test.

  - Cách thu thập dữ liệu:
    - Dữ liệu thu thập từ hơn 30 người tình nguyện tại thành phố Quảng Ngãi và Quảng Nam.
    - Nhóm sẽ gọp chung 30 mẫu dữ liệu với nhóm của bạn Đặng Văn Minh --> data train: là 60 mẫu, còn lại nhóm sẽ giữ để làm data test riêng cho nhóm.
    - Nhóm sẽ chuẩn bị sẵn các mầu tờ giấy và sẽ nhờ những tình nguyện viên viết những con chữ vào ô tờ giấy như **Hình 1**
![](Image/data.jpg)

