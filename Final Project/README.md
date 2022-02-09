<h1 align="center"><b>ĐỀ TÀI: SỐ HÓA TỦ SÁCH (BOOKCASE DIGITIZATION)</b></h>
<h1 align="center"><b>LỚP: CS114.M11.KHCL</b></h>

# **1.Giới thiệu**
* **Giảng viên:**
  * Lê Đình Duy
  * Phạm Nguyễn Trường An
* **Thành viên nhóm:**
  * Lê Đình Đức - 19521372 (Leader)
  * Phan Anh Lộc - 19521766
  * Lưu Anh Dũng - 19521392
 
# **2.Mô tả bài toán**
* **Bối cảnh ứng dụng:** Có thể giải quyết được việc thay vì thao tác nhập tay để lưu thông tin của quyển sách ta có thể đọc từ ảnh chụp.
* **Input:** Ảnh chụp bìa 1 cuốn sách từ camera
* **Output:** 1 file csv gồm các trường dữ liệu sau:
  * Tên file
  * Tên cuốn sách
  * Tên tác giả
  * Nhà xuất bản
  * Tập
  * Người dịch
  * Tải bản

# **3.Mô tả dữ liệu**
* **Thu nhập dữ liệu:**
  * Bộ test: Khoảng 400 ảnh bìa sách được chụp từ camera
  * Bộ train + validation: Dự tính khoảng 8000 ảnh bìa sách được crawl từ nhiều nguồn khác nhau trên mạng
### **3.1 Thu thập dữ liệu:**
  * 234 ảnh bìa sách được chụp dưới nền đen.
  * 7269 ảnh bìa sách được crawl từ nhiều nguồn khác nhau như:
    * [Nhà xuất bản Trẻ](https://www.nxbtre.com.vn/)
    * [Nhà xuất bản Kim Đồng](https://nxbkimdong.com.vn/)
    * [Nhà xuất bản ĐHQG-TPHCM](https://vnuhcmpress.edu.vn/)
    * ...
  * 22954 dòng text được cắt ra từ chính những sách đã thu thập được.
  * 100000 dòng text được lấy từ github VietOCR (Do có quá nhiều ảnh nên nhóm chỉ up lên 25000/100000 tấm demo, nhóm sẽ up file nén rar nếu thầy muốn xem toàn bộ 100k tấm)

### **3.2 Dán nhãn dữ liệu**
  * 7269 ảnh bìa sách phục vụ train model YOLO ([link dán nhãn](http://makesense.ai/))
  * Hơn 20000 dòng text để phục vụ train model [VietOCR](https://github.com/pbcquoc/vietocr) ([link dán nhãn](https://www.robots.ox.ac.uk/~vgg/software/via/via.html))

### **3.3 Thao tác xử lý dữ liệu:**
  * Đầu tiên với ảnh thô chụp từ camera dưới nền đen ta contour ảnh từ một số bước xử lý dữ liệu:
    * Resize ảnh.
    * Convert ảnh thành Gray Scale.
    * Sử dụng Gaussian Blur và Candy Blur.
    * [Find contour](https://pythonexamples.org/python-opencv-cv2-find-contours-in-image/).
    * Lấy ra contour lớn nhất.
    * Lấy ra bốn điểm của countour và cắt ảnh bằng [cv2.warpPerspective](https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87)

  * Tiếp theo đến việc detect object, nhóm sử dụng model deeplearning của [YOLOv5](https://github.com/ultralytics/yolov5)
      * Với 6 label:
        * 0: Tên sách
        * 1: Tên tác giả
        * 2: Nhà xuất bản
        * 3: Tập
        * 4: Người dịch
        * 5: Tái bản
      * Cắt ảnh ra từ những object đã được predict của phần object detection ở trên.
  * Craft:
    * Nhóm sử dụng model deeplearning đã được train sẵn từ nhiều ngôn ngữ khác nhau: [Craft text detector](https://github.com/clovaai/CRAFT-pytorch)
  * OCR:
    * Chuyển ảnh thành Gray Scale.
    * Nhóm sử dụng model [VietOCR](https://github.com/pbcquoc/vietocr).
    * Sử dụng xoay ảnh để có thể đọc được cả chữ dọc.
    * Xử lý xóa các text không liên quan trong tên sách do các object khác nhau bị chồng lên nhau, ví dụ như trong việc tên sách có cả tên tác giả nếu như trong object tên sách có cả tên tác giả thì ta sẽ xóa tên tác giả có trong tên sách.
  * Lưu kết quả:
    * Thêm vào dataframe và lưu dưới dạng file csv.

### **3.4 Phân chia (split)**
 * Với model YOLOv5 
    * Training data: 6269 labels
    * Validation data: 1000 labels
 * Với model VietOCR thì nhóm để chia train/val theo tỉ lệ 80/20.
 * Đối với việc đánh giá thì nhóm dành những ảnh chụp thực tế chưa dán nhãn cả phần VietOCR và YOLO gồm 234 tấm ảnh
 ## **4.Data:**
 * Data YOLO: https://drive.google.com/drive/folders/1aHMmGXyXRp35Snn0jwMDmhnt6c5Z7Fl_?usp=sharing
 * Data OCR: https://drive.google.com/drive/folders/1k-fcbl1xsN5XaAv0BE6mitnINXoF-h7J?usp=sharing
 * Data đánh giá model (234 tấm): https://drive.google.com/drive/folders/1wNWmA_LfoPS_364SvuBX9kUdwnB4FdQH?usp=sharing
