#1.function進階用法:function A執行function B
import cv2
def print_1():
    print("1")
def show_image():
    img = cv2.imread("Lenna.jpg")
    cv2.imshow("win",img)
    cv2.waitKey(0)
def show_hello():
    print("hello")
def number(Number):
    if Number == 1:
        print_1()                                               #呼叫function要有「()」，若不是則不需要「()」
    elif Number == 3:
        show_image()                                            #呼叫function要有「()」，若不是則不需要「()」
    elif Number == 5:
        show_hello()                                            #呼叫function要有「()」，若不是則不需要「()」
    else:
        return "顯示錯誤"
Number = int(input("請輸入數字0-5: "))                           #function和input連結:輸入的數字會執行function
number(Number)


#2.function進階用法:使用append將function加入list
import cv2
def print_1():
    print("1")
def show_image():
    img = cv2.imread("Lenna.jpg")
    cv2.imshow("win",img)
    cv2.waitKey(0)
def show_hello():
    print("hello")
def show_error():
    print("error")
def operation():    
    Number = int(input("請輸入數字0-5: "))
    List = []
    for i in range(6):
        List.append(show_error)                                 #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」加入6個「show_error函式」，接著在特定位置用其他函示取代;呼叫function要有「()」，若不是則不需要「()」
    List[1] = print_1                                           #在List[1]用「print_1函式」取代「show_error函式」;呼叫function要有「()」，若不是則不需要「()」
    List[3] = show_image                                        #在List[3]用「print_1函式」取代「show_image函式」;呼叫function要有「()」，若不是則不需要「()」
    List[5] = show_hello                                        #在List[5]用「print_1函式」取代「show_hello函式」;呼叫function要有「()」，若不是則不需要「()」
    List[Number]()                                              #list和input連結:輸入的數字會執行list裡的function;呼叫function要有「()」，若不是則不需要「()」
operation()


#3.function進階用法:try-except
import cv2
def print_1():
    print("1")
def show_image():
    img = cv2.imread("Lenna.jpg")
    cv2.imshow("win",img)
    cv2.waitKey(0)
def show_hello():
    print("hello")
def show_error():
    print("error")
def operation():    
    Number = int(input("請輸入數字0-5: "))
    try:
        if Number == 1:
            print_1()
        elif Number == 3:
            show_image()
        elif Number == 5:
            show_hello() 
        else:
            raise ValueError("顯示錯誤")                         #'raise 「Error類型」(「要表達之文字」)'
    except ValueError as A:                                     #'except 「Error類型」 as 「變數」:'
        print(A)
operation()


#4.function進階用法:使用append將function加入list搭配try-except
import cv2
def print_1():
    print("1")
def show_image():
    img = cv2.imread("Lenna.jpg")
    cv2.imshow("win",img)
    cv2.waitKey(0)
def show_hello():
    print("hello")
def show_error():
    print("error")
def operation():    
    Number = int(input("請輸入數字0-5: "))
    List = []
    for i in range(6):
        List.append(show_error)                                 #「append」除了可以將「文字或數字」加入「list」，也可以將「照片」或是「函式」加入:利用「append」加入6個「show_error函式」，接著在特定位置用其他函示取代;呼叫function要有「()」，若不是則不需要「()」
    List[1] = print_1                                           #在List[1]用「print_1函式」取代「show_error函式」;呼叫function要有「()」，若不是則不需要「()」
    List[3] = show_image                                        #在List[3]用「print_1函式」取代「show_image函式」;呼叫function要有「()」，若不是則不需要「()」
    List[5] = show_hello                                        #在List[5]用「print_1函式」取代「show_hello函式」;呼叫function要有「()」，若不是則不需要「()」
    try:
        List[Number]()                                          #list和input連結:輸入的數字會執行list裡的function;呼叫function要有「()」，若不是則不需要「()」;try盡量簡短，因此可能出錯的才放此
    except:
        show_error()
operation()


#5.function進階用法:if __name__ == "__main__"
if __name__ == "__main__":                                      #若其他人要引用此py檔不會執行「if __name__ == "__main__"」下方的程式
    operation()
    
    
    
    
    
    
    