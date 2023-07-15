# 1.putText() 加入文字(1)
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
# img 來源影像
# text 文字內容
# org 文字座標 ( 垂直方向是文字底部到影像頂端的距離 )
# fontFace 文字字型
# fontScale 文字尺寸
# color 線條顏色，使用 BGR
# thickness 文字外框線條粗細，預設 1
# lineType 外框線條樣式，預設 cv2.LINE_8，設定 cv2.LINE_AA 可以反鋸齒


# 2.putText() 加入文字(2)
import cv2
import numpy as np
img = np.zeros((150,300,3), dtype = "uint8")   # 建立 300x150 的黑色畫布
text = "Hello"
org = (20,90)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0,0,255)
thickness = 5
lineType = cv2.LINE_AA
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.putText() 加入文字(3)
import cv2
import numpy as np
img = np.zeros((150,300,3), dtype = "uint8")   # 建立 300x150 的黑色畫布
try:
    text = "Hello"
    org = (20,90)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2.5
    color = (0,0,255)
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
    cv2.imshow("test", img)
    cv2.waitKey(0)      # 按下任意鍵停止
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 4.使用中文字型(1)
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image    # 載入 PIL 相關函式庫
img = np.zeros((150,300,3), dtype = "uint8")   # 繪製黑色畫布
fontpath = "NotoSansTC-Regular.otf"          # 設定字型路徑
font = ImageFont.truetype(fontpath, 50)      # 設定字型與文字大小
imgPil = Image.fromarray(img)                # 將 img 轉換成 PIL 影像
draw = ImageDraw.Draw(imgPil)                # 準備開始畫畫
draw.text((0, 0), "大家好～\n嘿嘿嘿～", fill = (255, 255, 255), font = font)  # 畫入文字，\n 表示換行
img = np.array(imgPil)                       # 將 PIL 影像轉換成 numpy 陣列
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5.使用中文字型(2)
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image    # 載入 PIL 相關函式庫
try:
    img = np.zeros((150,300,3), dtype = "uint8")   # 繪製黑色畫布
    fontpath = "NotoSansTC-Regular.otf"          # 設定字型路徑
    font = ImageFont.truetype(fontpath, 50)      # 設定字型與文字大小
    imgPil = Image.fromarray(img)                # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)                # 準備開始畫畫
    draw.text((0, 0), "大家好～\n嘿嘿嘿～", fill = (255, 255, 255), font = font)  # 畫入文字，\n 表示換行
    img = np.array(imgPil)                       # 將 PIL 影像轉換成 numpy 陣列
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")













































