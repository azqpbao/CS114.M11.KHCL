import scanner
import yolov5
import crop_line_and_ocr
import sys, getopt

pathImage = ''

# dùng lệnh !python main.py - i <input folder> để tiện hơn cho việc sử dụng
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
  
  # scanner ảnh từ ảnh có nền đen thành ảnh bìa sách không còn nền đen
  images, fn = scanner.scanner(pathImage)
  # lấy object và cache
  obj = yolov5.object_detection(images)
  # ocr thông tin trong ảnh
  dataframe = crop_line_and_ocr.craft_and_ocr(obj, fn)
  # save to csv
  dataframe.to_csv('data.csv', header=True)
