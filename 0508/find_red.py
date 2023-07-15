import cv2
import numpy as np


img = cv2.imread("Lenna.jpg")
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(hueImage, lowRange, highRange)       #cv2.inRange(img, lowerb, upperb):指定一個色彩的最低數值與最高數值(使用「NumPy」陣列)，抓取符合這個色彩範圍內的所有像素成為新影像(範圍外的像素都會被過濾掉)
print(mask[0][0])
print(mask[0][150])
cv2.imshow('mask', mask)
res = cv2.bitwise_and(img, img, mask=mask)              #使用bitwise_and()以及加入「mask」參數，將img以及mask做交集運算並遮罩;因為mask以及img channel數不同，所以交集運算並遮罩時，前兩個參數要放相同image，第三個參數才放mask，若channel數相同則只需要前兩個參數即可
cv2.imshow('Input', img)
cv2.imshow('Result', res)
cv2.waitKey(0)
#while cv2.waitKey(100) != 27: #27 is esc ascii code
    #if cv2.getWindowProperty("Input",cv2.WND_PROP_VISIBLE)<=0:
        #break             #Linux使用