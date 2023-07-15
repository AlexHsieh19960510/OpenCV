#1.影像轉灰階
import cv2
img = cv2.imread("Lenna.jpg")
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("win",newImg)
cv2.waitKey(0)


#2.影像轉RGB
import cv2
img = cv2.imread("Lenna.jpg")
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("win",newImg)
cv2.waitKey(0)


#3.輸入數值決定影像轉灰階或RGB
import cv2
x = int(input("please set number: "))
img = cv2.imread("Lenna.jpg")
if x == 1:                                                         #「if-else」判斷輸入的值
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                   #轉RGB
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
elif x == 2:                                                       #「if-else」判斷輸入的值
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                  #灰階
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
elif x == 3:                                                       #「if-else」判斷輸入的值
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
else:
    print("error")


#4.輸入數值決定function執行:影像轉灰階或RGB
import cv2
def bgr_to_rgb(img):                                               #轉RGB的function
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def bgr_to_gray(image):                                            #灰階的function
    newImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def show_origin(image):
    cv2.imshow("win",image)
    cv2.waitKey(0)
x = int(input("please set number: "))   
img = cv2.imread("Lenna.jpg")
if x == 1:                                                         #「if-else」判斷輸入的值
    bgr_to_rgb(img)
elif x == 2:                                                       #「if-else」判斷輸入的值
    bgr_to_gray(img)
elif x == 3:                                                       #「if-else」判斷輸入的值
    show_origin(img)
else:
    print("error")


#5.啟動function以輸入數值決定function執行:影像轉灰階或RGB
import cv2
def bgr_to_rgb(image):                                             #轉RGB的function
    newImg = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def bgr_to_gray(image):                                            #灰階的function
    newImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def show_origin(image):
    cv2.imshow("win",image)
    cv2.waitKey(0)
def way_2():                                                       #輸入數值的function
    x = int(input("please set number: ")) 
    img = cv2.imread("Lenna.jpg")
    if x == 1:                                                     #「if-else」判斷輸入的值
        bgr_to_rgb(img)
    elif x == 2:                                                   #「if-else」判斷輸入的值
        bgr_to_gray(img)
    elif x == 3:                                                   #「if-else」判斷輸入的值
        show_origin(img)
    else:
        print("error")
way_2()


#6.啟動function以輸入數值決定function執行:影像轉灰階或RGB(設定跟執行分開)
import cv2
def bgr_to_rgb(image):                                             #轉RGB的function
    newImg = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def bgr_to_gray(image):
    newImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)                #灰階的function
    cv2.imshow("win",newImg)
    cv2.waitKey(0)
def show_origin(image):
    cv2.imshow("win",image)
    cv2.waitKey(0)
def null(image):                                                   #空的function
    return
def way_3():                                                       #輸入數值的function
    x = int(input("please set number: ")) #-1
    img = cv2.imread("Lenna.jpg")
    #selectionLists = [null,bgr_to_rgb,bgr_to_gray,show_origin]    #將function丟到list裡
    #selectionLists[x](img)                                        #用offset以及(img)達到上述if-else的判斷
    
    #不想list太長
    #selectionLists = []
    #selectionLists.append(null)                                   #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」一個個將函示加入list，若最前方加入「null函式」，則「input之數值」不用「-1」;呼叫function要有「()」，若不是則不需要「()」          
    #selectionLists.append(bgr_to_rgb)                             #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」一個個將函示加入list，若最前方加入「null函式」，則「input之數值」不用「-1」;呼叫function要有「()」，若不是則不需要「()」
    #selectionLists.append(bgr_to_gray)                            #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」一個個將函示加入list，若最前方加入「null函式」，則「input之數值」不用「-1」;呼叫function要有「()」，若不是則不需要「()」
    #selectionLists.append(show_origin)                            #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」一個個將函示加入list，若最前方加入「null函式」，則「input之數值」不用「-1」;呼叫function要有「()」，若不是則不需要「()」

    #不想append太多次
    selectionLists = []
    for i in range(4):
        selectionLists.append(null)                                #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」加入4個「null函式」，接著在特定位置用其他函示取代;呼叫function要有「()」，若不是則不需要「()」
    selectionLists[1] = bgr_to_rgb                                 #在selectionLists[1]用「bgr_to_rgb函式」取代「null函式」;呼叫function要有「()」，若不是則不需要「()」
    selectionLists[2] = bgr_to_gray                                #在selectionLists[2]用「bgr_to_gray函式」取代「null函式」;呼叫function要有「()」，若不是則不需要「()」
    selectionLists[3] = show_origin                                #在selectionLists[3]用「show_origin函式」取代「null函式」;呼叫function要有「()」，若不是則不需要「()」
way_3()