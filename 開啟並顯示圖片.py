# 1.imread() 開啟圖片(1)
import cv2
img = cv2.imread("meme.jpg")   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imshow("oxxostudio", img)  # 使用名為 oxxostudio 的視窗開啟圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗


# 2.imread() 開啟圖片(2)
import cv2
img = cv2.imread("meme.jpg")   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
try:
    cv2.imshow("oxxo", img)  # 使用名為 oxxostudio 的視窗開啟圖片
    cv2.waitKey(0)                 # 按下任意鍵停止
    cv2.destroyAllWindows()        # 結束所有圖片視窗
except:
    print("找不到圖片")

# 3.imread() 開啟圖片(3)
import cv2
img = cv2.imread("meme.jpg", cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
# img = cv2.imread('meme.jpg', 2) # 也可使用數字代表模式
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4.imread() 開啟圖片(4)
import cv2
img = cv2.imread("meme.jpg", cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
# img = cv2.imread('meme.jpg', 2) # 也可使用數字代表模式
try:
    cv2.imshow("oxxo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("找不到圖片")


# 5.imshow() 顯示圖片
# imshow() 包含兩個參數，第一個參數為字串，表示要開啟圖片的視窗名稱，第二個參數為使用 imread() 讀取的圖片。


# 6.waitKey() 等待多久關閉(1)
import cv2
img = cv2.imread("meme.jpg", cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
cv2.imshow("oxxostudio", img)
cv2.waitKey(2000)       # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗
cv2.destroyAllWindows()


# 7.waitKey() 等待多久關閉(2)
# 數字	        模式	                        說明
#   1	cv2.IMREAD_UNCHANGED	        原本的圖像（ 如果圖像有 alpha 通道則會包含 )。
#   2	cv2.IMREAD_GRAYSCALE	        灰階圖像。
#   3	cv2.IMREAD_COLOR	            BGR 彩色圖像。
#   4	cv2.IMREAD_ANYDEPTH	            具有對應的深度時返回 16/32 位元圖像，否則將其轉換為 8 位元圖像。
#   5	cv2.IMREAD_ANYCOLOR	            以任何可能的顏色格式讀取圖像。
#   6	cv2.IMREAD_LOAD_GDAL	        使用 gdal 驅動程式加載圖像。
#   7	cv2.IMREAD_REDUCED_GRAYSCALE_2	灰階圖像，圖像尺寸減小 1/2。
#   8	cv2.IMREAD_REDUCED_COLOR_2	    BGR 彩色圖像，圖像尺寸減小 1/2。
#   9	cv2.IMREAD_REDUCED_GRAYSCALE_4	灰階圖像，圖像尺寸縮小 1/4。
#   10	cv2.IMREAD_REDUCED_COLOR_4	    BGR 彩色圖像，圖像尺寸減小 1/4。
#   11	cv2.IMREAD_REDUCED_GRAYSCALE_8	灰階圖像，圖像尺寸縮小 1/8。
#   12	cv2.IMREAD_REDUCED_COLOR_8	    BGR 彩色圖像，圖像尺寸減小 1/8。
#   13	cv2.IMREAD_IGNORE_ORIENTATION	不要根據 EXIF 資訊的方向標誌旋轉圖像。




























