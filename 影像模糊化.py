# 1.blur() 平均模糊(1)
# cv2.blur(img, ksize)
# img 來源影像
# ksize 指定區域單位


# 2.blur() 平均模糊(2)
import cv2
img = cv2.imread("meme.jpg")
output1 = cv2.blur(img, (5, 5))     # 指定區域單位為 (5, 5)
output2 = cv2.blur(img, (25, 25))   # 指定區域單位為 (25, 25)
cv2.imshow("oxxostudio1", output1)
cv2.imshow("oxxostudio2", output2)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()


# 3.GaussianBlur() 高斯模糊(1)
# cv2.GaussianBlur(img, ksize, sigmaX, sigmaY)
# img 來源影像
# ksize 指定區域單位 ( 必須是大於 1 的奇數 )
# sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0


# 4.GaussianBlur() 高斯模糊(2)
import cv2
img = cv2.imread("meme.jpg")
output1 = cv2.GaussianBlur(img, (5, 5), 0)   # 指定區域單位為 (5, 5)
output2 = cv2.GaussianBlur(img, (25, 25), 0) # 指定區域單位為 (25, 25)
cv2.imshow("oxxostudio1", output1)
cv2.imshow("oxxostudio2", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5.medianBlur() 中值模糊(1)
# cv2.medianBlur(img, ksize)
# img 來源影像
# ksize 模糊程度 ( 必須是大於 1 的奇數 )


# 6.medianBlur() 中值模糊(2)
import cv2
img = cv2.imread("meme.jpg")
output1 = cv2.medianBlur(img, 5)   # 模糊程度為 5
output2 = cv2.medianBlur(img, 25)  # 模糊程度為 25
cv2.imshow("oxxostudio1", output1)
cv2.imshow("oxxostudio2", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 7.bilateralFilter() 雙邊模糊(1)
# cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)
# img 來源影像
# d 相鄰像素的直徑，預設使用 5，數值越大運算的速度越慢
# sigmaColor 相鄰像素的顏色混合，數值越大，會混合更多區域的顏色，並產生更大區塊的同一種顏色
# sigmaSpace 會影響像素的區域，數值越大，影響的範圍就越大，影響的像素就越多


# 8.bilateralFilter() 雙邊模糊(2)
import cv2
img = cv2.imread("meme.jpg")
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)
cv2.imshow("oxxostudio1", output1)
cv2.imshow("oxxostudio2", output2)
cv2.imshow("oxxostudio3", output3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 9.影片的模糊效果
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
    # 套用 medianBlur() 中值模糊
    img = cv2.medianBlur(frame, 25)
    cv2.imshow("oxxostudio", img)
    if cv2.waitKey(1) == ord("q"):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
