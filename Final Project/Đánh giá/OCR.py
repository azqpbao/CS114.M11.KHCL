# import craft functions
from craft_text_detector import (
    read_image,
    load_craftnet_model,
    load_refinenet_model,
    get_prediction,
)
from craft_text_detector.file_utils import rectify_poly
from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import pandas as pd
import cv2

def ocr(i, detector):
    if i.shape[0] < i.shape[1]:
        i = Image.fromarray(i)
        s, p = detector.predict(i, return_prob = True)
        if p > 0.7:
            return (s, p)
        else:
            return (0, 0)
    else:
        im1 = Image.fromarray(i)
        s1, p1 = detector.predict(im1, return_prob = True)
        s = s1
        p = p1

        im2 = cv2.rotate(i, cv2.ROTATE_90_CLOCKWISE)
        im2 = Image.fromarray(im2)
        s2, p2 = detector.predict(im2, return_prob = True)
        if p2 > p:
            p = p2
            s = s2

        im3 = cv2.rotate(i, cv2.ROTATE_90_COUNTERCLOCKWISE)
        im3 = Image.fromarray(im3)
        s3, p3 = detector.predict(im3, return_prob = True)
        if p3 > p:
            p = p3
            s = s3
        if p > 0.7:
            return (s, p)
        else:
            return (0, 0)
        
#sort chữ khi crop line
def sort_img(regions):
    for i in range(len(regions) - 1):
        min = i
        for j in range(i, len(regions)):
            if abs(regions[min][0, 1] - regions[j][0, 1]) > 10:
                if regions[min][0, 1] > regions[j][0, 1]:
                    min = j
            else:
                if regions[min][0, 0] > regions[j][0, 0]:
                    min = j
        regions[min], regions[i] = regions[i], regions[min]
    return regions
    
def read(img, key, craft_net, refine_net, detector):
    image = read_image(img)
    #predict craft
    if key == 0:
        prediction_result = get_prediction(
          image=image,
          craft_net=craft_net,
          refine_net=refine_net,
          text_threshold=0.7,
          link_threshold=0.4,
          low_text=0.4,
          cuda=True,    
          long_size=1280
      )
    elif key == 3:
        prediction_result = get_prediction(
            image=image,
            craft_net=craft_net,
            refine_net=refine_net,
            text_threshold=0.7,
            link_threshold=0.1,
            low_text=0.1,
            cuda=True,
            long_size=1280
        )
    else:
        prediction_result = get_prediction(
          image=image,
          craft_net=craft_net,
          refine_net=refine_net,
          text_threshold=0.7,
          link_threshold=0.1,
          low_text=0.2,
          cuda=True,
          long_size=1280
      )
    regions=prediction_result["polys"]
    sort_img(regions)
    a = []
    for i in regions:
        a.append(rectify_poly(image, i))
    p = 0
    s = ''
    for i in a:
        s_temp, p_temp = ocr(i, detector)
        if s_temp != 0:
            p += p_temp
            s += s_temp + " "
        p = p/len(a)
    return s, p

def craft_and_ocr(results, fn):
    # load model
    refine_net = load_refinenet_model(cuda=True)
    craft_net = load_craftnet_model(cuda=True)
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = '/content/gdrive/MyDrive/Final_Project_CS114/Training_result/transformerocr.pth'
    config['cnn']['pretrained']=False
    config['device'] = 'cuda:0'
    config['predictor']['beamsearch']=False
    detector = Predictor(config)
    out = []
    idx = 0
    # predict OCR
    for info, cache in results:
        ten_sach = ""
        ten_tac_gia = ""
        nha_xuat_ban = ""
        tap = ""
        nguoi_dich = ""
        tai_ban = ""
        for key, value in info.items():
            for img in value:
                if img.shape[0] < img.shape[1] * 2:
                    s, _ = read(img, key, craft_net, refine_net, detector)
                    if key == 0:
                        ten_sach += s + " "
                    elif key == 1:
                        ten_tac_gia += s + " "
                    elif key == 2:
                        nha_xuat_ban += s + " "
                    elif key == 3:
                        tap += s + " "
                    elif key == 4:
                        nguoi_dich += s + " "
                    else:
                        tai_ban += s + " "
                else:
                    im1 = img
                    s1, p1 = read(img, key, craft_net, refine_net, detector)
                    s = s1
                    p = p1
                    im2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                    s2, p2 = read(im2, key, craft_net, refine_net, detector)
                    if p2 > p:
                        p = p2
                        s = s2
                    im3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    s3, p3 = read(im3, key, craft_net, refine_net, detector)
                    if p3 > p:
                        p = p3
                        s = s3
                    if key == 0:
                        ten_sach += s + " "
                    elif key == 1:
                        ten_tac_gia += s + " "
                    elif key == 2:
                        nha_xuat_ban += s + " "
                    elif key == 3:
                        tap += s + " "
                    elif key == 4:
                        nguoi_dich += s + " "
                    else:
                        tai_ban += s + " "
        # kiểm tra xem các nhãn khác có bị lẫn vào tên sách không, có thì lấy nó ra
        for i in cache:
            if i == 1:
                if ten_tac_gia in ten_sach:
                    ten_sach = ten_sach.replace(ten_tac_gia, '')
                else:
                    for s in ten_tac_gia.split():
                        ten_sach = ten_sach.replace(s, '')
            elif i == 2:
                if nha_xuat_ban in ten_sach:
                    ten_sach = ten_sach.replace(nha_xuat_ban, '')
                else:
                    for s in nha_xuat_ban.split():
                        ten_sach = ten_sach.replace(s, '')
            elif i == 3:
                if tap in ten_sach:
                    ten_sach = ten_sach.replace(tap, '')
                else:
                    for s in tap.split():
                        ten_sach = ten_sach.replace(s, '')
            elif i == 4:
                if nguoi_dich in ten_sach:
                    ten_sach = ten_sach.replace(nguoi_dich, '')
                else:
                    for s in nguoi_dich.split():
                        ten_sach = ten_sach.replace(s, '')
            elif i == 5:
                if tai_ban in ten_sach:
                    ten_sach = ten_sach.replace(tai_ban, '')
                else:
                    for s in tai_ban.split():
                        ten_sach = ten_sach.replace(s, '')
        
        #thêm vào dictionary
        features = {
            'file names' : fn[idx],
            'tên sách': ten_sach,
            'tên tác giả': ten_tac_gia,
            'nhà xuất bản': nha_xuat_ban,
            'tập': tap,
            'người dịch': nguoi_dich,
            'tái bản': tai_ban
        }
        idx += 1
        out.append(features)
    #tạo dataframe và lưu vào
    output = pd.DataFrame()
    output = output.append(out, sort=False)
    output = output.sort_values(by=['file names'])
    return output
