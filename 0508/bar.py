#1.bar值改變圓的大小:保留畫圓前的照片並保留當前的圓
import cv2
circleRadius = 1
def update(x):
    print(x)
    global circleRadius                                                         #要先global呼叫才能做後續運算
    circleRadius = x
img = cv2.imread("Lenna.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)
center = (100,100)
color = (255,0,0)
thickness = 2
while True:
    circleImg = img.copy()                                                      #保留畫圓前圖片
    cv2.circle(circleImg,center,circleRadius,color,thickness)                   #用複製的照片畫圓
    cv2.imshow("win",circleImg)
    x = cv2.waitKey(100)
    if x == 27:
        break
        

#2.bar值改變才會顯示圖像以及畫圓:保留畫圓前的照片並保留當前的圓
import cv2
circleRadius = 1
def update(x):
    print(x)
    global circleRadius
    circleRadius = x
    circleImg = img.copy()                                                      #保留畫圓前圖片
    cv2.circle(circleImg,center,circleRadius,color,thickness)                   #用複製的照片畫圓
    cv2.imshow("win",circleImg)
img = cv2.imread("Lenna.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)
center = (100,100)
color = (255,0,0)
thickness = 2
while True:
    x = cv2.waitKey(100)
    if x == 27:
        break


#3.bar值改變圓的位置:保留畫圓前的照片並保留當前的圓
import cv2
changex = 1
changey = 1
def change_x(x):
    print(x)
    global changex                                                              #要先global呼叫才能做後續運算
    changex = x
def change_y(y):
    print(y)
    global changey                                                              #要先global呼叫才能做後續運算
    changey = y
img = cv2.imread("Lenna.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("x","win",1,300,change_x)
cv2.createTrackbar("y","win",1,300,change_y)
radius = 1
color = (255,0,0)
thickness = 2
while True:
    circleImg = img.copy()                                                      #保留畫圓前圖片
    #center = (changex,changey)
    cv2.circle(circleImg,(changex,changey),radius,color,thickness)              #用複製的照片畫圓
    cv2.imshow("win",circleImg)
    x = cv2.waitKey(100)
    if x == 27:
        break


#4.bar值改變圓的顏色:保留畫圓前的照片並保留當前的圓
import cv2
changeB = 0
changeG = 0
changeR = 0
def change_B(x):
    print(x)
    global changeB                                                              #要先global呼叫才能做後續運算                      
    changeB = x
def change_G(y):
    print(y)
    global changeG                                                              #要先global呼叫才能做後續運算                       
    changeG = y
def change_R(z):
    print(z)
    global changeR                                                              #要先global呼叫才能做後續運算                     
    changeR = z
img = cv2.imread("Lenna.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("x","win",0,255,change_B)
cv2.createTrackbar("y","win",0,255,change_G)
cv2.createTrackbar("z","win",0,255,change_R)
center = (100,100)
radius = 1
thickness = 10
while True:
    circleImg = img.copy()                                                      #保留畫圓前圖片
    cv2.circle(circleImg,center,radius,(changeB,changeG,changeR),thickness)     #用複製的照片畫圓
    cv2.imshow("win",circleImg)
    x = cv2.waitKey(100)
    if x == 27:
        break


