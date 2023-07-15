# 1.在視窗中加入滑桿(1)
# cv2.createTrackbar("滑桿名稱", "視窗名稱", min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式

# cv2.setTrackbarPos("滑桿名稱","視窗名稱", val)
# val 滑桿預設值


# 2.在視窗中加入滑桿(2)
import cv2

img = cv2.imread("mona.jpg")
cv2.imshow("oxxostudio", img)

def test(val):
    print(val)

cv2.createTrackbar("test", "oxxostudio", 0, 255, test)
cv2.setTrackbarPos("test", "oxxostudio", 50)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()


# 3.透過滑桿，調整影像亮度與對比度
import cv2
import numpy as np

img = cv2.imread("mona.jpg")
cv2.imshow("oxxostudio", img)

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow("oxxostudio", img)

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.imshow("oxxostudio", output)

# 定義調整亮度函式
def brightness_fn(val):
    global img, contrast, brightness
    brightness = val - 100
    adjust(img, contrast, brightness)

# 定義調整對比度函式
def contrast_fn(val):
    global img, contrast, brightness
    contrast = val - 100
    adjust(img, contrast, brightness)

cv2.createTrackbar("brightness", "oxxostudio", 0, 200, brightness_fn)  # 加入亮度調整滑桿
cv2.setTrackbarPos("brightness", "oxxostudio", 100)
cv2.createTrackbar("contrast", "oxxostudio", 0, 200, contrast_fn)      # 加入對比度調整滑桿
cv2.setTrackbarPos("contrast", "oxxostudio", 100)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()
