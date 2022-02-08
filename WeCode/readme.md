### **3.1 Thu thập dữ liệu:**
  * 500 ảnh bìa sách được chụp dưới nền đen.
  * 10000 ảnh bìa sách được crawl từ nhiều nguồn khác nhau như:
    * [Nhà xuất bản Trẻ](https://www.nxbtre.com.vn/)
    * [Nhà xuất bản Kim Đồng](https://nxbkimdong.com.vn/)
    * [Nhà xuất bản ĐHQG-TPHCM](https://vnuhcmpress.edu.vn/)
    * [Nhà xuất bản Hà Nội](http://www.nxbhanoi.com.vn/)
    * [Nhà xuất bản Đà Nẵng](https://nxbdanang.vn/)
    * [Nhà xuất bản Quân đội nhân dân](http://nxbqdnd.com.vn/)
    * [Nhà xuất bản khoa học xã hội](http://nxbkhxh.vass.gov.vn/)
    * [Nhà xuất bản thanh niên](https://www.nhaxuatbanthanhnien.vn/)
    * [Nhà xuất bản tư pháp](https://nxbtuphap.moj.gov.vn/)
    * [Nhà sách tiki](tiki.vn/sach-truyen-tieng-viet/c316?page=1&src=c.8322.hamburger_menu_fly_out_banner)
  * 45000 dòng text được cắt ra từ chính những sách đã thu thập được.
  * 100000 dòng text được generate từ nhiều font chữ khác nhau.

### **3.2 Dán nhãn dữ liệu**
  * Vì thời gian thực hiện đồ án có hạn nên nhóm em đã dán nhãn được:
    * 6000 ảnh bìa sách phục vụ train model YOLO ([link dán nhãn](http://makesense.ai/))
    * 45000 dòng text để phục vụ train model VietOCR ([link dán nhãn](https://www.robots.ox.ac.uk/~vgg/software/via/via.html))

### **3.3 Thao tác xử lý dữ liệu:**
  * Đầu tiên với ảnh thô chụp từ camera dưới nền đen ta dễ dàng contour ảnh từ một số bước xử lý dữ liệu:
    * Resize ảnh.
    * Convert ảnh thành Gray Scale.
    * Sử dụng Gaussian Blur và Candy Blur.
    * [Find contour](https://pythonexamples.org/python-opencv-cv2-find-contours-in-image/).
    * Lấy ra contour lớn nhất.
    * Lấy ra bốn điểm của countour và cắt ảnh bằng [cv2.warpPerspective](https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87)

  * Tiếp theo đến việc detect object, nhóm em sử dụng model deeplearning của [YOLOv5](https://github.com/ultralytics/yolov5)
      * Với 6 label:
        * 0: Tên sách
        * 1: Tên tác giả
        * 2: Nhà xuất bản
        * 3: Tập
        * 4: Người dịch
        * 5: Tái bản
      * Cắt ảnh ra từ những object đã được predict của phần object detection ở trên.
  * Craft:
    * Nhóm em sử dụng model deeplearning đã được train sẵn từ nhiều ngôn ngữ khác nhau: [Craft text detector](https://github.com/clovaai/CRAFT-pytorch) với:
      * text_threshold=0.7
      * link_threshold=0.4
      * low_text=0.3
      * long_size=1280
  * OCR:
    * Chuyển ảnh thành Gray Scale.
    * Nhóm em sử dụng model [VietOCR](https://github.com/pbcquoc/vietocr).
    * Sử dụng xoay ảnh để có thể đọc được cả chữ dọc.
    * Xử lý xóa các text không liên quan trong tên sách do các object khác nhau bị chồng lên nhau, ví dụ như trong việc tên sách có cả tên tác giả nếu như trong object tên sách có cả tên tác giả thì ta sẽ xóa tên tác giả có trong tên sách.
  * Lưu kết quả:
    * Thêm vào dataframe và lưu dưới dạng file csv.

### **3.4 Phân chia (split) - train/dev/test**
 * Với model YOLOv5 
    * Training data (85%): 5951 labels (tỉ lệ train/val là 8/2)​
        * Tập train: 4745 labels​
        * Tập val: 1206 labels​
    * Testing data (15%): 1031 labels
 * Với model VietOCR thì nhóm em để chia train/val theo tỉ lệ 80/20.
 * Đối với việc đánh giá thì em dành những ảnh chụp thực tế chưa dán nhãn cả phần VietOCR và YOLO chia làm 3 phần: easy(106), medium(147), hard(71)
 ## **4.Data:**
 * Data YOLO: https://drive.google.com/file/d/1wmFvdessDGsXND22T3sdgNaizbmzvqOT/view?usp=sharing
 * Data OCR: https://drive.google.com/uc?id=1LqaWeO2qOgZIO3LdrPtntOioQJWdwA-V
 ## **5.Trainning:** Quá trình trainning chia làm hai phần:
 * Object-detection (YOLO): <a href="https://colab.research.google.com/drive/1JnxkR9EeLXjfqhK-OlJXjkeWgB1yE1xP?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
 * OCR (VietOCR): <a href="https://colab.research.google.com/drive/1DG0j27Ll73Pw0z66NKS1zl56JhCFDigO?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>