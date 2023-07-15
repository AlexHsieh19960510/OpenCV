# 1.line() 畫直線(1)
# cv2.line(img, pt1, pt2, color, thickness)
# img 來源影像
# pt1 起始點座標 pt2 結束點座標
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1


# 2.line() 畫直線(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")   # 繪製 300x300 的黑色畫布
cv2.line(img,(50,50),(250,250),(0,0,255),5)  # 繪製線條
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.line() 畫直線(3)
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")   # 繪製 300x300 的黑色畫布
try:
    cv2.line(img,(50,50),(250,250),(0,0,255),5)  # 繪製線條
    cv2.imshow("test", img)
    cv2.waitKey(0)                               # 按下任意鍵停止
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 4.arrowedLine() 畫箭頭線條(1)
# cv2.arrowedLine(img, pt1, pt2, color, thickness, tipLength)
# img 來源影像
# pt1 起始點座標 pt2 結束點座標
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1
# tipLength 箭頭長度，預設 0.1 ( 箭頭線條長度 x 0.1 )


# 5.arrowedLine() 畫箭頭線條(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.arrowedLine(img,(50,50),(250,250),(0,0,255),5)  # 繪製箭頭線條
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 6.arrowedLine() 畫箭頭線條(3)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    cv2.arrowedLine(img,(50,50),(250,250),(0,0,255),5)  # 繪製箭頭線條
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 7.rectangle() 畫四邊形(1)
# cv2.rectangle(img, pt1, pt2, color, thickness)
# img 來源影像
# pt1 左上座標 pt2 右下座標
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1，設定 -1 表示填滿


# 8.rectangle() 畫四邊形(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.rectangle(img,(50,50),(250,250),(0,0,255),5)  # 繪製正方形
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 9.rectangle() 畫四邊形(3)
import cv2
import numpy as np
try:
    img = np.zeros((300,300,3), dtype = "uint8")
    cv2.rectangle(img,(50,50),(250,250),(0,0,255),5)  # 繪製正方形
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 10.rectangle() 畫四邊形(4)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.rectangle(img,(50,50),(250,250),(0,0,255),-1)  # 設定 -1
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 11.rectangle() 畫四邊形(5)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    cv2.rectangle(img,(50,50),(250,250),(0,0,255),-1)  # 設定 -1
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 12.rectangle() 畫四邊形(6)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
img[50:250, 50:250] = [0,0,255] # 將中間 200x200 的陣列內容改成 [0,0,255]
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 13.rectangle() 畫四邊形(7)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    img[50:250, 50:250] = [0,0,255] # 將中間 200x200 的陣列內容改成 [0,0,255]
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 14.circle() 畫圓形(1)
# cv2.circle(img, center, radius, color, thickness)
# img 來源影像
# center 中心點座標
# radius 半徑
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1，設定 -1 表示填滿


# 15.circle() 畫圓形(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.circle(img,(150,150),100,(0,0,255),5)  # 繪製圓形
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 16.circle() 畫圓形(3)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    cv2.circle(img,(150,150),100,(0,0,255),5)  # 繪製圓形
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 17.circle() 畫圓形(4)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.circle(img,(150,150),100,(0,0,255),-1)  # 設定 -1
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 18.circle() 畫圓形(5)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    cv2.circle(img,(150,150),100,(0,0,255),-1)  # 設定 -1
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 19.ellipse() 畫橢圓形(1)
# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
# img 來源影像
# center 中心點座標
# axes 長軸與短軸
# angle 轉向角度，正值逆時針，負值順時針
# startAngle 起始角度，endAngle 結束角度，範圍 0～360
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1，設定 -1 表示填滿


# 20.ellipse() 畫橢圓形(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
cv2.ellipse(img,(150,150),(100,50),45,0,360,(0,0,255),5)
cv2.ellipse(img,(150,150),(30,100),90,0,360,(255,150,0),5)
cv2.ellipse(img,(150,150),(20,120),30,0,360,(0,255,255),5)
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 21.ellipse() 畫橢圓形(3)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    cv2.ellipse(img,(150,150),(100,50),45,0,360,(0,0,255),5)
    cv2.ellipse(img,(150,150),(30,100),90,0,360,(255,150,0),5)
    cv2.ellipse(img,(150,150),(20,120),30,0,360,(0,255,255),5)
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 22.polylines() 畫多邊形(1)
# cv2.polylines(img, pts, isClosed, color, thickness)
# img 來源影像
# pts 座標陣列 ( 使用 numpy 陣列 )
# isClosed 多邊形是否閉合，True 閉合，False 不閉合
# color 線條顏色，使用 BGR
# thickness 線條粗細，預設 1


# 23.polylines() 畫多邊形(2)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
pts = np.array([[150,50],[250,100],[150,250],[50,100]])   # 產生座標陣列
cv2.polylines(img,[pts],True,(0,0,255),5)   # 繪製多邊形
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 24.polylines() 畫多邊形(3)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    pts = np.array([[150,50],[250,100],[150,250],[50,100]])   # 產生座標陣列
    cv2.polylines(img,[pts],True,(0,0,255),5)   # 繪製多邊形
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")


# 25.polylines() 畫多邊形(4)
# cv2.fillPoly(img, pts, color)
# img 來源影像
# pts 座標陣列 ( 使用 numpy 陣列 )
# color 線條顏色，使用 BGR


# 26.polylines() 畫多邊形(5)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
pts = np.array([[150,50],[250,100],[150,250],[50,100]])
cv2.fillPoly(img,[pts],(0,0,255))
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 27.polylines() 畫多邊形(6)
import cv2
import numpy as np
img = np.zeros((300,300,3), dtype = "uint8")
try:
    pts = np.array([[150,50],[250,100],[150,250],[50,100]])
    cv2.fillPoly(img,[pts],(0,0,255))
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("圖片有誤")











