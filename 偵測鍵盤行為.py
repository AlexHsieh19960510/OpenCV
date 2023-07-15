# 1.取得鍵盤按鍵的 ASCII 代碼
import cv2

cv2.namedWindow("oxxostudio")  # 建立一個名為 oxxostudio 的視窗

while True:
    keycode = cv2.waitKey(0)   # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(keycode)           # 將 ASCII 代碼轉換成真實字元
    print(c, keycode)          # 印出結果
    if keycode == 27:
        break                  # 如果代碼等於 27，結束迴圈 ( 27 表示按鍵 ESC )

cv2.destroyAllWindows()


# 2.透過鍵盤，調整影像的亮度和對比度
import cv2
import numpy as np

img = cv2.imread("mona.jpg")

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow("oxxostudio", img)

while True:
    keycode = cv2.waitKey(0)
    if keycode == 0:
        brightness = brightness + 5    # 按下鍵盤的「上」，增加亮度
    if keycode == 1:
        brightness = brightness - 5    # 按下鍵盤的「下」，減少亮度
    if keycode == 2:
        contrast = contrast - 5        # 按下鍵盤的「右」，增加對比度
    if keycode == 3:
        contrast = contrast + 5        # 按下鍵盤的「左」，減少對比度
    if keycode == 113:
        contrast, brightness = 0, 0    # 按下鍵盤的「q」，恢復預設值
    if keycode == 27:
        break
    show = img.copy()                  # 複製原始圖片
    show = adjust(show, contrast, brightness)  # 根據亮度和對比度的調整值，輸出新的圖片
    cv2.imshow("oxxostudio", show)

cv2.destroyAllWindows()
