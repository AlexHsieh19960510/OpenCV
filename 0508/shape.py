#影像之shape
import cv2
img = cv2.imread("Lenna.jpg")
h,w,c = img.shape                                              #「c」:channel
print("w is "+str(w)+",h is "+str(h)+", c is "+str(c))
print(img[0][0])


#灰階影像之shape
import cv2
img = cv2.imread("Lenna.jpg")
newImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
h,w,c = newImg.shape                                           #「c」:channel
print("w is "+str(w)+",h is "+str(h)+", c is "+str(c))         #跑不出來正常，因為由原本「RGB」「三維array」變成只有「gray」「一維的array」，但若照片一樣是來自「RGB三維」且只有「修改顏色值」，「shape」結果之「C」一樣會是「3」
print(newImg[0][0])