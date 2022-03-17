import cv2
import torch

def object_detection(images):
    # load model custom data yolov5l
    model = torch.hub.load('yolov5', 'custom', path='/content/gdrive/MyDrive/Final_Project_CS114/Training_result/last.pt', source='local')
    model.conf = 0.5
    results = []
    # cắt từng vùng ảnh tên sách, tên tác giả, nhà xuất bản, tập, người dịch, tái bản
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Inference
        pre = model(img, size=720)
        #lấy danh sách kết quả
        locate = pre.pandas().xyxy[0]
        ten_sach = []
        ten_tac_gia = []
        nha_xuat_ban = []
        tap = []
        nguoi_dich = []
        tai_ban = []
        lo = []
        #cắt từng vùng ảnh và thêm vảo mảng đã định danh
        for index, row in locate.iterrows():
            if row['class'] == 0:
                ten_sach.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            elif row['class'] == 1:
                ten_tac_gia.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            elif row['class'] == 2:
                nha_xuat_ban.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            elif row['class'] == 3:
                tap.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            elif row['class'] == 4:
                nguoi_dich.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            else:
                tai_ban.append(img[int(row['ymin']):int(row['ymax']), int(row['xmin']):int(row['xmax']), :])
            lo.append([row['class'], int(row['ymin']), int(row['ymax']), int(row['xmin']), int(row['xmax'])])
        # kiểm tra sự chồng chéo của các nhãn, nếu tác giả nằm trong vùng tên sách có thể loại bỏ tác giả ra khi pre tên sách
        cache = []
        length = len(lo)
        for i in range(length):
            if lo[i][0] != 0:
                continue
            index = lo[i]
            kq = []
            for j in range(length):
                for y, x in [(1, 3), (1, 4), (2, 3), (2, 4)]:
                    if index[1] < lo[j][y] and lo[j][y] < index[2] and index[3] < lo[j][x] and lo[j][x] < index[4]:
                        kq.append(lo[j][0])
                        break
            kq = set(kq)
            kq = list(kq)
            cache.extend(kq)
        #thêm vào dictionary
        features = {
            0: ten_sach,
            1: ten_tac_gia,
            2: nha_xuat_ban,
            3: tap,
            4: nguoi_dich,
            5: tai_ban
        }
        results.append([features, cache])
    return results
