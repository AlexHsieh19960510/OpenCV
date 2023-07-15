# 1.imwrite() 寫入並儲存圖片
import cv2
img = cv2.imread("meme.jpg", cv2.IMREAD_GRAYSCALE)   # 以灰階模式開啟圖片
cv2.imwrite("oxxostudio_2.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
cv2.imwrite("oxxostudio_3.png", img)  # 存成 png


# 2.儲存陣列產生的圖片(1)
import cv2
import numpy as np
img = np.zeros((500,500,3), dtype = "uint8")   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]
cv2.imwrite("oxxostudio.jpg", img)       # 存成 jpg
cv2.imshow("oxxostudio", img)            # 顯示圖片
cv2.waitKey(0)                           # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.儲存陣列產生的圖片(2)
import cv2
import numpy as np
img = np.zeros((500,500,3), dtype = "uint8")   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
try:
    img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]
    cv2.imshow("red box", img)            # 顯示圖片
    cv2.waitKey(0)                           # 按下任意鍵停止
    cv2.destroyAllWindows()
except:
    print("圖片有誤")












































