#1.批次畫四邊形:使用「for」迴圈
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]                                              
import cv2
img = cv2.imread("Lenna.jpg")
def show_result(img,a):
    for i in a:
        thickness = 1
        color = (0,255,0)
        point1, point2 = i[0:2], i[2:4]
        point1 = i[0],i[1]
        point2 = i[2],i[3] 
        cv2.rectangle(img,point1,point2,color,thickness)
        cv2.imshow("win",img)
    cv2.waitKey(0)                                                                                  #「waitKey」在「for」迴圈外才能只畫出一張圖，若在「for」迴圈內會畫出兩張圖
show_result(img,a)


#2.批次寫文字:使用「for」迴圈
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]               
import cv2
img = cv2.imread("Lenna.jpg")
def show_word(img,a):
    for i in a:
        position = i[0],i[1]
        position = i[2],i[3] 
        text = i[4]
        size = 1
        color = (0,255,255)
        lineWidth = 1
        cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)
        cv2.imshow("win",img)
    cv2.waitKey(0)                                                                                  #「waitKey」在「for」迴圈外才能只畫出一張圖，若在「for」迴圈內會畫出兩張圖
show_word(img,a)


#3.批次畫四邊形以及寫文字:使用「for」迴圈
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]               
import cv2
img = cv2.imread("Lenna.jpg")
def show_word(img,a):
    j=0
    for i in a: 
        j+=1
        text = str(j)+"."+i[4]                                                                      #寫文字搭配變數「j」可以有編號的效果
        position = (i[0],i[1]+50)
        size = 1
        color = (255,255,255)
        lineWidth = 1
        cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)
        cv2.imwrite("result.jpg",img)                                                               #雖然畫出兩隻圖但因為黨名相同所以會覆蓋
        cv2.imshow("win",img)
        cv2.waitKey(0)                                                                              #「waitKey」在「for」迴圈內會畫出兩張圖，若在「for」迴圈外才能只畫出一張圖
show_word(img,a)


#4.批次畫四邊形以及寫文字:使用「for」迴圈以及函式(1)
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]               
import cv2
img = cv2.imread("Lenna.jpg")
def draw_rectangle(i,img):
    point1 = i[0],i[1]
    point2 = i[2],i[3] 
    thickness = 1
    color = (0,255,0)
    cv2.rectangle(img,point1,point2,color,thickness)
    
def draw_text(i,j,img):
    text = str(j)+"."+i[4]
    position = (i[0],i[1]+50)
    size = 1
    color = (255,255,255)
    lineWidth = 1
    cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)
    
def is_save(bool):
    if bool == True:
        return cv2.imwrite("Final.jpg",img)                                                         #雖然各畫出兩張圖但因為黨名相同所以會覆蓋只產生一張同時有畫兩個四邊形以及寫兩個文字的影像
    pass

def show_result(img,a,bool):                                                                        #一影像先畫完四邊形再寫文字
    j=0
    for i in a:
        j+=1
        draw_rectangle(i,img)
        draw_text(i,j,img)
        is_save(bool)
        cv2.imshow("win",img)
        cv2.waitKey(0)                                                                              #「waitKey」在「for」迴圈內會畫出兩張圖，若在「for」迴圈外才能只畫出一張圖
show_result(img,a,True)


#5.批次畫四邊形以及寫文字:使用「for」迴圈以及函式(2)
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]               
import cv2
img = cv2.imread("Lenna.jpg")
newImg = img.copy()
def draw_rectangle(i,img):
    point1 = i[0],i[1]
    point2 = i[2],i[3] 
    thickness = 1
    color = (0,255,0)
    cv2.rectangle(img,point1,point2,color,thickness)
    
def draw_text(i,j,img):
    text = str(j)+"."+i[4]
    position = (i[0],i[1]+50)
    size = 1
    color = (255,255,255)
    lineWidth = 1
    cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)

def is_save(bool):
    if bool == True:
        return cv2.imwrite("rectangle.jpg",img),cv2.imwrite("text.jpg",newImg)                      #雖然各畫出兩張圖但因為黨名相同所以各會覆蓋產生一張同時有畫兩個四邊形以及一張寫兩個文字的影像
    pass
    
def show_result(img,a,bool):                                                                        #一影像畫四邊形另一影像寫文字
    j=1
    for i in a:
        j+=1
        draw_rectangle(i,img)
        draw_text(i,j,newImg)
        is_save(bool)
        cv2.imshow("win",img)
        cv2.waitKey(0)                                                                              #「waitKey」在「for」迴圈內會畫出兩張圖，若在「for」迴圈外才能只畫出一張圖
show_result(img,a,True)


#6.批次畫四邊形以及寫文字:使用「for」迴圈以及函式(3)
a=[[123,34,57,62,"cat"],[12,85,145,32,"dog"]]               
import cv2
img = cv2.imread("Lenna.jpg")
def draw_rectangle(i,img):
    point1 = i[0],i[1]
    point2 = i[2],i[3] 
    thickness = 1
    color = (0,255,0)
    cv2.rectangle(img,point1,point2,color,thickness)

def draw_text(i,j,img):
    text = str(j)+"."+i[4]
    position = (i[0],i[1]+50)
    size = 1
    color = (255,255,255)
    lineWidth = 1
    cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)

def is_save(j,bool):
    if bool == True:
        File_name = "Final"+str(j+20)+".jpg"                                                        #儲存檔名搭配變數「j」可以有編號的效果，因此每執行一次「for」迴圈，除存檔名都不同
        return cv2.imwrite(File_name,img)
    
def show_result(img,a,bool):                                                                        #一影像先畫完四邊形再寫文字
    j=0
    for i in a:
        j+=1
        draw_rectangle(i,img)
        draw_text(i,j,img)
        cv2.imshow("win",img)
        is_save(j,bool)
        '''if bool == True:
            File_name = "Final"+str(j)+".jpg"
            cv2.imwrite(File_name,img)
            #cv2.imwrite(str(j)+"result.jpg",img)
            #cv2.imwrite("result"+str(j)+".jpg",img)'''
        cv2.waitKey(0)                                                                              #「waitKey」在「for」迴圈內會畫出兩張圖，若在「for」迴圈外才能只畫出一張圖
show_result(img,a,True)
