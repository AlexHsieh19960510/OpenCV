# 1.shape 取得長寬與色版數量
import cv2
img = cv2.imread("meme.jpg")
print(img.shape)            # 得到 (360, 480, 3)
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)              # 按下任意鍵停止
cv2.destroyAllWindows()


# 2.size 取得像素總數
import cv2
img = cv2.imread("meme.jpg")
print(img.size)            # 518400 ( 360x480x3 )
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 3.dtype 取得數據類型
import cv2
img = cv2.imread("meme.jpg")
print(img.dtype)            # uint8
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4.取得每個像素的色彩資訊(1)
import cv2
img = cv2.imread("meme-test.png")
print(img)
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5.取得每個像素的色彩資訊(2)
import cv2
img = cv2.imread("meme-test.png")
b, g, r = cv2.split(img)
print(b)
print(g)
print(r)
cv2.imshow("oxxostudio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 6.取得每個像素的色彩資訊(3)
import cv2
img_blue = cv2.imread("meme.jpg")
img_green = cv2.imread("meme.jpg")
img_red = cv2.imread("meme.jpg")
img_blue[:,:,1] = 0    # 將綠色設為 0
img_blue[:,:,2] = 0    # 將紅色設為 0
img_green[:,:,0] = 0   # 將藍色設為 0
img_green[:,:,2] = 0   # 將紅色設為 0
img_red[:,:,0] = 0     # 將藍色設為 0
img_red[:,:,1] = 0     # 將綠色設為 0
cv2.imshow("oxxostudio blue", img_blue)
cv2.imshow("oxxostudio green", img_green)
cv2.imshow("oxxostudio red", img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()


































