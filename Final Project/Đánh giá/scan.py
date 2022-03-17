import cv2
import numpy as np
import os

heightImg = 720
widthImg = 540

# lấy 4 điểm từ contour
def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype = np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

# tìm contour lớn nhất
def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 5000:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area

def scanner(pathImage):
    FJoin = os.path.join
    files = [FJoin(pathImage, f) for f in os.listdir(pathImage)]
    images = []
    for path in files:
        img = cv2.imread(path)
        img = cv2.resize(img, None, fx = 0.3, fy = 0.3)  
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)  
        imgThreshold = cv2.Canny(imgBlur, 30, 50)  
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(imgThreshold, kernel, iterations = 2)  
        imgThreshold = cv2.erode(imgDial, kernel, iterations = 1)  
        # tìm tất cả contour
        contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)  
        # lấy contour lớn nhất
        biggest, maxArea = biggestContour(contours)
        if biggest.size != 0:
            biggest = reorder(biggest)
            pts1 = np.float32(biggest) 
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) # từ biggestContour vừa tìm đc, tiến hành cắt bìa sách
            images.append(imgWarpColored)
        else:
            print('not scanner image ', path)   
            img = cv2.resize(img, (widthImg, heightImg))
            images.append(img)
    return (images, os.listdir(pathImage)) 
