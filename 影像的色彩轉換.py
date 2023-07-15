# 1.色彩模型(1)
# RGB ( 紅、綠、藍 )
# 將紅 ( Red )、綠 ( Green )、藍 ( Blue ) 三原色的色光以不同的比例相加，混合產生各種色彩的光線，通常表現方式會使用 (255,255,255) 或十六進位 FFFFFF 來表現。


# 2.色彩模型(2)
# RGBA ( 紅、綠、藍、alpha )
# RGBA 代表紅 ( Red )、綠 ( Green )、藍 ( Blue ) 和 Alpha 通道，alpha 通道為影像的不透明度參數，數值可以用百分比、整數或者使用 0 到 1 的實數表示。


# 3.色彩模型(3)
# HSV ( 色相、飽和度、明度 )、HSL ( 色相、飽和度、亮度 )
# HSL 和 HSV 顏色模型都是一種將 RGB 色彩模型中的點，轉變在圓柱坐標系中的表示法。HSL 是色相、飽和度、亮度 ( Hue、Saturation、Lightness )，HSV 是色相、飽和度、明度 ( Hue、Saturation、Value )，又稱 HSB ( Brightness )。
# HSL 和 HSV 模型都把顏色描述在圓柱坐標系內的點，這個圓柱的中心軸取值為自底部的黑色到頂部的白色而在它們中間的是灰色，繞這個軸的角度對應於「色相」，到這個軸的距離對應於「飽和度」，而沿著這個軸的高度對應於「亮度」、「色調」或「明度」。


# 4.色彩模型(4)
# GRAY ( 灰階 )
# 用於顯示的灰階影像，通常用每個採樣像素 8bits 的非線性尺度，內容可以包含 256 種灰階。


# 5.cvtcolor() 色彩轉換(1)
# cv2.cvtColor(img, code)
# img 來源影像
# code 要轉換的色彩空間名稱


# 6.cvtcolor() 色彩轉換(2)
#       代碼	            說明
# cv2.COLOR_BGR2BGRA	RGB 轉 RGBA。
# cv2.COLOR_BGRA2BGR	RGBA 轉 RGB。
# cv2.COLOR_BGR2GRAY	RGB 轉灰階。
# cv2.COLOR_BGR2HSV	    RGB 轉 HSV。
# cv2.COLOR_RGB2HLS	    RGB 轉 RSL。


# 7.cvtcolor() 色彩轉換(3)
import cv2
img = cv2.imread("meme.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
cv2.imwrite("oxxo", img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()


# 8.cvtcolor() 色彩轉換(4)
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
    cv2.imshow("oxxostudio", gray)
    if cv2.waitKey(1) == ord("q"):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()































