#1.畫圓
import cv2
img = cv2.imread("Lenna.jpg")
cv2.imshow("win",img)
center = (180,160)
radius = 10
color = (0,0,255)
newImg = cv2.circle(img,center,radius,color,2)                                                  #「thickness」:'2'改'-1'變實心
cv2.imshow("win",newImg)
cv2.waitKey(0)


#2.保留畫圓前的照片並保留所有圓:用函式
import cv2
img = cv2.imread("Lenna.jpg")
def show_circle(center,color,img):
    radius = 10
    originImg = img.copy()                                                                      #保留畫圓前之圖片
    cv2.circle(img,center,radius,color,2)                                                       #用原始照片畫圓
    cv2.imshow("win",img)
    cv2.imshow("win1",originImg)
    cv2.waitKey(0)
center = (180,160)
color = (0,0,255)    
show_circle(center,color,img)
show_circle((160,180),(255,0,0),img)                                                            #保留紅色圓
show_circle((170,170),(0,255,0),img)                                                            #保留紅色以及藍色的圓


#3.保留畫圓前的照片並保留當前的圓:用函式
import cv2
img = cv2.imread("Lenna.jpg")
def show_circle(center,color,img):
    radius = 10
    originImg = img.copy()                                                                      #保留畫圓前之圖片                                                                                                                             
    cv2.circle(originImg,center,radius,color,2)                                                 #用複製的照片畫圓
    #cv2.imshow("win",img)
    cv2.imshow("win1",originImg)
    cv2.waitKey(0)
center = (180,160)
color = (0,0,255)    
show_circle(center,color,img)
show_circle((160,180),(255,0,0),img)                                                            #只有藍色的圓，紅色圓不見
show_circle((170,170),(0,255,0),img)                                                            #只有綠色的圓，藍色圓以及紅色圓不見


#4.畫四邊形
import cv2
def show_rectangle():
    img = cv2.imread("Lenna.jpg")
    point1 = (180,160)
    point2 = (20,50)
    thickness = 1
    color = (0,255,0)
    cv2.rectangle(img,point1,point2,color,thickness)
    cv2.imshow("win",img)
    cv2.waitKey(0)
show_rectangle()


#5.寫字
import cv2
def show_word():
    img = cv2.imread("Lenna.jpg")
    position = (10,40)
    size = 1
    color = (0,255,255)
    lineWidth = 1
    cv2.putText(img,"hello",position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)
    cv2.imshow("win",img)
    cv2.waitKey(0)
show_word()

      