# 1.inrange() 抓取特定範圍顏色(1)
# cv2.inRange(img, lowerb, upperb)
# img 來源影像
# 色彩範圍最低數值
# 色彩範圍最高數值


# 2.inrange() 抓取特定範圍顏色(2)
import cv2
import numpy as np
lower = np.array([30,40,200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255]) # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
img = cv2.imread("oxxo.jpg")
mask = cv2.inRange(img, lower, upper)             # 使用 inRange
output = cv2.bitwise_and(img, img, mask = mask )  # 套用影像遮罩
cv2.imwrite("output.jpg", output)
cv2.waitKey(0)                                    # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.即時抓取影片的特定顏色
import cv2
import numpy as np
lower = np.array([30,40,200])   # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    mask = cv2.inRange(frame, lower, upper)               # 使用 inRange
    output = cv2.bitwise_and(frame, frame, mask = mask )  # 套用影像遮罩
    cv2.imshow("oxxostudio", output)
    if cv2.waitKey(1) == ord("q"):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
