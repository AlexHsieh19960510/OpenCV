# 1.偵測滑鼠事件
import cv2
img = cv2.imread("meme.jpg")

def show_xy(event,x,y,flags,userdata):
    print(event,x,y,flags)
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式

cv2.imshow("oxxostudio", img)
cv2.setMouseCallback("oxxostudio", show_xy)  # 設定偵測事件的函式與視窗

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()


# 2.滑鼠 event 與 flag 列表
# 代號	        事件	               說明
#   0	cv2.EVENT_MOUSEMOVE	          滑動
#   1	cv2.EVENT_LBUTTONDOWN	    左鍵點擊
#   2	cv2.EVENT_RBUTTONDOWN	    右鍵點擊
#   3	cv2.EVENT_MBUTTONDOWN	    中鍵點擊
#   4	cv2.EVENT_LBUTTONUP	        左鍵放開
#   5	cv2.EVENT_RBUTTONUP	        右鍵放開
#   6	cv2.EVENT_MBUTTONUP	        中鍵放開
#   7	cv2.EVENT_LBUTTONDBLCLK	    左鍵雙擊
#   8	cv2.EVENT_RBUTTONDBLCLK	    右鍵雙擊
#   9	cv2.EVENT_MBUTTONDBLCLK	    中鍵雙擊

# 代號	            flag	           說明
#   1	    cv2.EVENT_FLAG_LBUTTON	 左鍵拖曳
#   2	    cv2.EVENT_FLAG_RBUTTON	 右鍵拖曳
#   4	    cv2.EVENT_FLAG_MBUTTON	 中鍵拖曳
# 8～15	    cv2.EVENT_FLAG_CTRLKEY	按 Ctrl 不放事件
# 16～31	cv2.EVENT_FLAG_SHIFTKEY	按 Shift 不放事件
# 32～39	cv2.EVENT_FLAG_ALTKEY	按 Alt 不放事件


# 3.透過滑鼠點擊，取得像素的顏色
import cv2
img = cv2.imread("meme.jpg")

def show_xy(event,x,y,flags,param):
    if event == 0:
        img2 = img.copy()                         # 當滑鼠移動時，複製原本的圖片
        cv2.circle(img2, (x,y), 10, (0,0,0), 1)   # 繪製黑色空心圓
        cv2.imshow("oxxostudio", img2)            # 顯示繪製後的影像
    if event == 1:
        color = img[y,x]                          # 當滑鼠點擊時
        print(color)                              # 印出顏色

cv2.imshow("oxxostudio", img)
cv2.setMouseCallback("oxxostudio", show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 4.透過滑鼠點擊，繪製多邊形
import cv2
img = cv2.imread("meme.jpg")

dots = []   # 記錄座標的空串列
def show_xy(event,x,y,flags,param):
    if event == 1:
        dots.append([x, y])                          # 記錄座標
        cv2.circle(img, (x, y), 10, (0,0,255), -1)   # 在點擊的位置，繪製圓形
        num = len(dots)                              # 目前有幾個座標
        if num > 1:                                  # 如果有兩個點以上
            x1 = dots[num-2][0]
            y1 = dots[num-2][1]
            x2 = dots[num-1][0]
            y2 = dots[num-1][1]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)  # 取得最後的兩個座標，繪製直線
        cv2.imshow("oxxostudio", img)

cv2.imshow("oxxostudio", img)
cv2.setMouseCallback("oxxostudio", show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
