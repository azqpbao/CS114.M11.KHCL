# Mô tả đồ án cuối kì
**Danh sách thành viên trong nhóm:**
+ Lê Đình Đức - 19521372
+ Phan Anh Lộc - 19521766
+ Lưu Anh Dũng - 19521392

## Đề tài: Phân loại bình luận tiếng Anh của một sản phẩm trên Youtube
**Lí do chọn đề tài: Với lượng dữ liệu văn bản được mở rộng trên nền tảng của Youtube, các bộ lọc hiện tại chưa cung cấp đủ các công cụ để phân loại sắc thái bình luận: nhận biết, ưu tiên các bình luận mang sắc thái tích cực, trung tính và ngăn chặn sự lây lan của các bình luận tiêu cực, ngôn từ kích động,thù địch**

**->Tạo 1 mô hình phân biệt bình luận tích cực, tiêu cực hay trung tính, từ đó tránh bị ảnh hưởng bởi các ngôn từ kích động, thù địch. Những bình luận tiêu cực thường có những từ ngữ không lành mạnh, thô tục,...nhằm hướng vào những mục tiêu khác nhau**

**Mô tả bài toán:**
+ Input: Một câu bình luận dưới dạng text
+ Output: Nhãn 1,2 hoặc 3 (với 1 là tích cực, 2 là trung tính, 3 là tiêu cực)

**Mô tả bộ dữ liệu**
+ Bộ dữ liệu: Crawl data trên 1 video nào đó trên Youtube
+ Ngôn ngữ sử dụng: Tiếng Anh

**Mục tiêu: Mục tiêu đặt ra của bài toán là xây dựng một bộ dữ liệu các bình luận về một sản phẩm trên nền tảng Youtube. Từ đó, áp dụng các mô hình học máy hiện đại để phân loại cảm xúc (emotion classification) các bình luận của người dùng Youtube về sản phẩm bằng cách phân loại các bình luận theo ba loại cảm xúc: tích cực (positive), tiêu cực (negative), trung tính (neutral)**

**Đánh giá mô hình: Dựa vào 4 thông số bao gồm: accuracy, precision, recall, F1-score (mong muốn tối thiếu 75%)**
