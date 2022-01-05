import cv2
import numpy as np
import Utlis as utlis
import os

########################################################################
heightImg = 720
widthImg = 540
########################################################################

def scanner(pathImage):
    # lấy path file ảnh từ đường dẫn đến folder chứa ảnh
    FJoin = os.path.join
    files = [FJoin(pathImage, f) for f in os.listdir(pathImage)]

    images = []
    
   
    for path in files:
        img = cv2.imread(path)
        img = cv2.resize(img, None, fx = 0.3, fy = 0.3)  # RESIZE ảnh
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT ảnh thành GRAY SCALE
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)  # GAUSSIAN BLUR
        imgThreshold = cv2.Canny(imgBlur, 30, 50)  # CANNY BLUR
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(imgThreshold, kernel, iterations = 2)  # APPLY DILATION
        imgThreshold = cv2.erode(imgDial, kernel, iterations = 1)  # APPLY EROSION

        # tìm tất cả countour
        contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)  

        # lấy countour lớn nhất
        biggest, maxArea = utlis.biggestContour(contours)
        if biggest.size != 0:
            biggest = utlis.reorder(biggest)
            pts1 = np.float32(biggest) 
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))# cắt bìa sách từ BIGEST COUNTOUR tìm được
            images.append(imgWarpColored)
        else:
            # Nếu không tìm thấy COUNTOUR thì ta vẫn thêm ảnh gốc vào nhưng sẽ in ra màng hình ảnh không contour được để cảnh báo
            print('not scanner image ', path)
            img = cv2.resize(img, (widthImg, heightImg))
            images.append(img)

    return (images, os.listdir(pathImage)) 
