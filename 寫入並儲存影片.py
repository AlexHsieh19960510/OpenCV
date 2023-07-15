# 1.使用 VideoWriter() 儲存影片
import cv2
cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fourcc = cv2.VideoWriter_fourcc(*"MJPG")          # 設定影片的格式為 MJPG
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (width,  height))  # 產生空的影片
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    out.write(frame)       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow("oxxostudio", frame)
    if cv2.waitKey(1) == ord("q"):
        break             # 按下 q 鍵停止
cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()


# 2.解決無法儲存影片的問題
# 實作過程中，可能會遇到「無法儲存影片」的狀況，通常的解決方法有下面三種：
# 修改 fourcc 的影片格式，如果是 mov 或 mp4 的影片檔，使用「＊"mp4v"」、「＊"MJPG"」或「"M","J","P","G"」( 星號改半形 )。
# 將輸入影片的長寬和輸入的長寬度調整為「相同的長寬」。
# 修改影片的檔名，加上 01、02、03...等數字。


# 3.搭配 cvtColor() 儲存為黑白的影片
import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("output.mov", fourcc, 20.0, (width,  height))
# 如果轉換成黑白影片後如果無法開啟，請加上 isColor=False 參數設定
# out = cv2.VideoWriter('output.mov', fourcc, 20.0, (width,  height), isColor=False)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    out.write(gray)
    cv2.imshow("oxxostudio", gray)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()


# 3.get 方法可取得的影片屬性
# 數字	        屬性	                    說明
#   0	cv.CAP_PROP_POS_MSEC	    影片目前播放的毫秒數。
#   1	cv.CAP_PROP_POS_FRAMES	    從 0 開始的被截取或解碼的幀的索引值。
#   2	cv.CAP_PROP_POS_AVI_RATIO	影片播放的相對位置，0 表示開始，1 表示結束。
#   3	cv.CAP_PROP_FRAME_WIDTH	    影片宽度。
#   4	cv.CAP_PROP_FRAME_HEIGHT	影片高度。
#   5	cv.CAP_PROP_FPS	影片幀率     fps。
#   6	cv.CAP_PROP_FOURCC	        編解碼的的四個字元。
#   7	cv.CAP_PROP_FRAME_COUNT	    影片總共有幾幀。
#   8	cv.CAP_PROP_FORMAT	        影片格式。
#   9	cv.CAP_PROP_MODE	        目前的截取模式。
#   10	cv.CAP_PROP_BRIGHTNESS	    攝影機亮度。
#   11	cv.CAP_PROP_CONTRAST	    攝影機對比度。
#   12	cv.CAP_PROP_SATURATION	    攝影機飽和度。
#   13	cv.CAP_PROP_HUE	            攝影機 HUE 色調數值。
#   14	cv.CAP_PROP_GAIN	        攝影機圖像增益數值。
#   15	cv.CAP_PROP_EXPOSURE	    攝影機曝光度。
#   16	cv.CAP_PROP_CONVERT_RGB	    影片是否有轉換為 RGB。

