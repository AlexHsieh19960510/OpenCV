#1.讀取影像以及取得影像之b、g、r
print("hello")
import cv2
img = cv2.imread("Lenna.jpg")
b,g,r = cv2.split(img)
print(b)
print(g)
print(r)
cv2.imshow("image",img)                       
cv2.waitKey(0)                                


#2.使用input讀取影像
import cv2
img=int(input("請輸入1或2: "))
if img == 1:
    img_lenna=cv2.imread("Lenna.jpg")
    cv2.imshow("Lenna",img_lenna)
    cv2.waitKey(0)
else:
    img_corgi=cv2.imread("corgi.jpg")
    cv2.imshow("corgi",img_corgi)
    cv2.waitKey(0)


#3.使用input讀取影像:使用list以及append
import cv2
A=[]
A.append("C:\Users\USER\Desktop\0508\Lenn1a.jpg")                    #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入，然而不建議先「imread」再「append」，因為「imread」的結果檔案很大;若圖片放在資料夾裡前面要加'「資料夾名稱」\':「相對路徑」，或是用terminal內的路徑:「絕對路徑」(「\」改為「/」);因為python「\」後面接某些英文會有其他功能，所以怕失敗可以用「\\」
A.append("C:\Users\USER\Desktop\0508\corgi.jpg")                     #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入，然而不建議先「imread」再「append」，因為「imread」的結果檔案很大;若圖片放在資料夾裡前面要加'「資料夾名稱」\':「相對路徑」，或是用terminal內的路徑:「絕對路徑」(「\」改為「/」);因為python「\」後面接某些英文會有其他功能，所以怕失敗可以用「\\」
value=int(input("請輸入數字1或2: "))
img=cv2.imread(A[value-1])                                           #利用「list」以不用「for迴圈」以及「if-else」方法將「input」出的結果帶入其他程式
cv2.imshow("Picture",img)
cv2.waitKey(0)

