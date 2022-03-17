import scan
import YOLOv5
import OCR
import sys, getopt

pathImage = ''

def main(argv):
    global pathImage
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifolder="])
    except getopt.GetoptError:
        print('main.py -i <inputfolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfolder>')
            sys.exit()
        elif opt in ("-i", "--ifolder"):
            pathImage = arg

if __name__ == "__main__":
    main(sys.argv[1:])
    # scan ảnh 
    images, fn = scan.scanner(pathImage)
    # lấy object và cache
    obj = YOLOv5.object_detection(images)
    # OCR thông tin trong ảnh
    dataframe = OCR.craft_and_ocr(obj, fn)
    # Lưu kết quả vào file csv
    dataframe.to_csv('result.csv', header=True)
