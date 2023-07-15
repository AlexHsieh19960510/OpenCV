# 1.bitwise_and() 交集(1)
# cv2.bitwise_and(img1, img2, mask)
# img1 第一張圖
# img2 第二張圖
# mask 遮罩影像 ( 非必須 )


# 2.bitwise_and() 交集(2)
import cv2
img1 = cv2.imread("test1.png")
img2 = cv2.imread("test2.png")
output = cv2.bitwise_and(img1, img2)  # 使用 bitwise_and
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.bitwise_or() 聯集(1)
# cv2.bitwise_or(img1, img2, mask)
# img1 第一張圖
# img2 第二張圖
# mask 遮罩影像 ( 非必須 )


# 4.bitwise_or() 聯集(2)
import cv2
img1 = cv2.imread("test1.png")
img2 = cv2.imread("test2.png")
output = cv2.bitwise_or(img1, img2)  # 使用 bitwise_or
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5.bitwise_xor() 差集(1)
# cv2.bitwise_or(img1, img2, mask)
# img1 第一張圖
# img2 第二張圖
# mask 遮罩影像 ( 非必須 )


# 6.bitwise_xor() 差集(2)
import cv2
img1 = cv2.imread("test1.png")
img2 = cv2.imread("test2.png")
output = cv2.bitwise_xor(img1, img2)  # 使用 bitwise_xor
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 7.bitwise_not() 非(1)
# cv2.bitwise_or(img)
# img 來源圖片
# mask 遮罩影像 ( 非必須 )


# 8.bitwise_not() 非(2)
import cv2
img1 = cv2.imread("test1.png")
output = cv2.bitwise_not(img1)  # 使用 bitwise_not
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 9.使用 mask 參數
import cv2
img1 = cv2.imread("test1.png")
img2 = cv2.imread("test2.png")
mask = cv2.imread("mask.png")                    # 遮罩圖片
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)    # 轉換成灰階模式
output = cv2.bitwise_xor(img1, img2, mask = mask)  # 加入 mask 參數
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 10.圖片去背與合成
import cv2
import numpy as np

logo = cv2.imread("logo.jpg")                    # 讀取 OpenCV 的 logo
size = logo.shape                                # 讀取 logo 的長寬尺寸

img = np.zeros((360,480,3), dtype = "uint8")       # 產生一張 480x360 背景全黑的圖
img[0:360, 0:480] = "255"                        # 將圖片變成白色 ( 配合 logo 是白色底 )
img[0:size[0], 0:size[1]] = logo                 # 將圖片的指定區域，換成 logo 的圖案
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 產生一張灰階的圖片作為遮罩使用
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)  # 使用二值化的方法，產生黑白遮罩圖片
logo = cv2.bitwise_and(img, img, mask = mask1 )  # logo 套用遮罩

bg = cv2.imread("meme.jpg")                      # 讀取底圖
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)      # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask = mask2 )      # 底圖套用遮罩

output = cv2.add(bg, logo)                       # 使用 add 方法將底圖和 logo 合併
cv2.imshow("oxxostudio", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 11.影片的遮罩效果(1)
import cv2
import numpy as np

logo = cv2.imread("logo.jpg")
size = logo.shape
img = np.zeros((360,600,3), dtype = "uint8")
img[0:360, 0:600] = "255"
img[0:size[0], 0:size[1]] = logo
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask = mask1 )
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))   # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask = mask2 )
    output = cv2.add(bg, logo)
    cv2.imshow("oxxostudio", output)
    if cv2.waitKey(1) == ord("q"):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()


# 12.影片的遮罩效果(2)
import cv2
import numpy as np

logo = cv2.imread("logo.jpg")
size = logo.shape
img = np.zeros((360,600,3), dtype = "uint8")
img[0:360, 0:600] = "255"
img[30:30+size[0], 155:155+size[1]] = logo         # 將 logo 置中
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))
    output = cv2.bitwise_not(frame, mask = mask1 )      # 套用 not 和遮罩
    output = cv2.bitwise_not(output, mask = mask1 )     # 再次套用 not 和遮罩，將色彩轉成原來的顏色
    cv2.imshow("oxxostudio", output)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

