import cv2
def to_gray(img):
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",newImg)

def to_rgb(img):  
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("rgb",newImg)

def template(algorithm):
    print("hello")
    img = cv2.imread("Lenna.jpg")
    algorithm(img)                                  #function A透過其參數執行function B:「algorithm」= 「其他function」
    cv2.waitKey(0)
template(to_rgb)                                    #「algorithm」= 「to_rgb」


'''def template1():
    print("hello")
    img = cv2.imread("Lenna.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",img)
    cv2.waitKey(0)
template(template1)

def template2():
    print("hello")
    img = cv2.imread("Lenna.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("rgb",img)
    cv2.waitKey(0)
template(template2)'''