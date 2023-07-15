# 1.VideoCapture() 開啟影片(1)
import cv2
cap = cv2.VideoCapture(0)         # 讀取攝影鏡頭
cap = cv2.VideoCapture("影片路徑") # 讀取電腦中的影片


# 2.VideoCapture() 開啟影片(2)
import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


# 3.VideoCapture() 開啟影片(3)
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


# 4.VideoCapture() 開啟影片(4)
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()             # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    cv2.imshow("oxxostudio", frame)     # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == ord("q"):      # 每一毫秒更新一次，直到按下 q 結束
        break
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗


# 5.VideoCapture() 開啟影片(5)
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()             # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    cv2.imshow("frame", frame)     # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == ord("q"):      # 每一毫秒更新一次，直到按下 q 結束
        break
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗


# 6.搭配 cvtColor() 改變影片色彩(1)
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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    # gray = cv2.cvtColor(frame, 6)  # 也可以用數字對照 6 表示轉換成灰階
    cv2.imshow("oxxostudio", gray)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


# 7.搭配 cvtColor() 改變影片色彩(2)
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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



















