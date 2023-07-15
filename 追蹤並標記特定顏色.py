# 1.抓取特定顏色，移除顏色內的雜訊
import cv2
import numpy as np
lower = np.array([30,40,200])   # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))           # 縮小尺寸，加快處理速度
    output = cv2.inRange(img, lower, upper)   # 取得顏色範圍的顏色
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(output, kernel)       # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)        # 縮小影像，還原大小

    cv2.imshow("oxxostudio", output)
    if cv2.waitKey(1) == ord("q"):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()


# 2.取得顏色範圍的輪廓座標
import cv2
import numpy as np
lower = np.array([30,40,200])
upper = np.array([90,100,255])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列，cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 使用 for 迴圈印出座標長相
    for contour in contours:
        print(contour)

    cv2.imshow("oxxostudio", output)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


# 3.根據輪廓座標，繪製形狀(1)
import cv2
import numpy as np
lower = np.array([30,40,200])
upper = np.array([90,100,255])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)    # 取得範圍內的面積
        color = (0,0,255)                  # 設定外框顏色
        # 如果面積大於 300 再標記，避免標記到背景中太小的東西
        if area > 300:
            for i in range(len(contour)):
                if i > 0 and i < len(contour) - 1:
                    # 從第二個點開始畫線
                    img = cv2.line(img, (contour[i-1][0][0], contour[i-1][0][1]), (contour[i][0][0], contour[i][0][1]), color, 3)
                elif i == len(contour) - 1:
                    # 如果是最後一個點，與第一個點連成一線
                    img = cv2.line(img, (contour[i][0][0], contour[i][0][1]), (contour[0][0][0], contour[0][0][1]), color, 3)

    cv2.imshow("oxxostudio", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


# 4.根據輪廓座標，繪製形狀(2)
import cv2
import numpy as np
lower = np.array([30,40,200])   # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0,0,255)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)                      # 取得座標與長寬尺寸
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)  # 繪製四邊形

    cv2.imshow("oxxostudio", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


# 5.同時追蹤並標記多種顏色
import cv2
import numpy as np
lower = np.array([30,40,200])
upper = np.array([90,100,255])

blue_lower = np.array([90,100,0])     # 設定藍色最低值範圍
blue_upper = np.array([200,160,100])  # 設定藍色最高值範圍

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0,0,255)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    # 設定選取藍色的程式
    blue_output = cv2.inRange(img, blue_lower, blue_upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    blue_output = cv2.dilate(blue_output, kernel)
    blue_output = cv2.erode(blue_output, kernel)
    contours, hierarchy = cv2.findContours(blue_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (255,255,0)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    cv2.imshow("oxxostudio", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
