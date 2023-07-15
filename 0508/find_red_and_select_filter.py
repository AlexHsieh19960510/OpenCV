#1.追蹤特定顏色並根據輪廓畫四邊形
import cv2
import numpy as np

img = cv2.imread("point_card.png")
cv2.imshow("before",img)
img = cv2.medianBlur(img,5)                            
cv2.imshow("after",img)
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(hueImage, lowRange, highRange)
mask = cv2.medianBlur(mask,5)

#RETR_EXTERNAL 只取最外層的輪廓
#RETR_LIST     取所有的輪廓
#CHAIN_APPROX_NONE  儲存所有輪廓點
#CHAIN_APPROX_SIMPLE  每一個方向只取一的點，四邊形只有四個點
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 獲得contours, 以及輪廓在第幾層(hierarchy, 通常不用)

for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt) #輪廓的四個點
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

cv2.imshow('result', img)
cv2.waitKey(0)
#while cv2.waitKey(100) != 27: #27 is esc ascii code
    #if cv2.getWindowProperty("result",cv2.WND_PROP_VISIBLE)<=0:
        #break


#2.追蹤特定顏色並根據輪廓畫四邊形以及在中心圓形
import cv2
import numpy as np

img = cv2.imread("point_card.png")
cv2.imshow("before",img)
img = cv2.medianBlur(img,5)                            
cv2.imshow("after",img)
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(hueImage, lowRange, highRange)
mask = cv2.medianBlur(mask,5)

#RETR_EXTERNAL 只取最外層的輪廓
#RETR_LIST     取所有的輪廓
#CHAIN_APPROX_NONE  儲存所有輪廓點
#CHAIN_APPROX_SIMPLE  每一個方向只取一的點，四邊形只有四個點
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 獲得contours, 以及輪廓在第幾層(hierarchy, 通常不用)

n=1
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt) #輪廓的四個點;x=左上點，y=右下點，w=長，h=寬
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    center = int((x+x+w)/2),int((y+y+h)/2)
    radius = 5
    color = (0,0,255)
    cv2.circle(img,center,radius,color,2)            
    print(n) #可以得知幾個點
    n+=1

cv2.imshow('result', img)
cv2.waitKey(0)
#while cv2.waitKey(100) != 27: #27 is esc ascii code
    #if cv2.getWindowProperty("result",cv2.WND_PROP_VISIBLE)<=0:
        #break
