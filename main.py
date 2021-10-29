import cv2
import numpy as np
def empty(a):
     pass

cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",800,240)
cv2.createTrackbar("Area val","trackBars",0,500,empty)


def getcontours(img):
        contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
                area= cv2.contourArea(cnt)
                print(area)
                area_val = cv2.getTrackbarPos("Area val", "trackBars")
                if area > area_val:
                        cv2.drawContours(imgcontours,cnt,-1,(255,0,0),3)
                        peri=cv2.arcLength(cnt,True)
                        ##print(peri)
                        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                        ##print(len(approx))
                        objCor= len(approx)
                        x ,y,w,h =cv2.boundingRect((approx))
                        if objCor ==3: objectType="Tri"

                        cv2.rectangle(imgcontours,(x,y),(x+w,y+h),(0,255,0),2)


cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",800,240)

cv2.createTrackbar("Hue min","trackBars",0,179,empty)
cv2.createTrackbar("Hue max","trackBars",179,179,empty)
cv2.createTrackbar("Sat min","trackBars",0,255,empty)
cv2.createTrackbar("Sat max","trackBars",255,255,empty)
cv2.createTrackbar("Val min","trackBars",0,255,empty)
cv2.createTrackbar("Val max","trackBars",204,255,empty)
cv2.createTrackbar("blur","trackBars",0,50,empty)

img = cv2.imread("d://result2.png")

img2=cv2.resize(img,(320,240))
img3=cv2.resize(img,(320,240))
imgcontours=img2.copy()
imgGray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
imgcanny=cv2.Canny(imgGray,50,50)
##cv2.imshow("Gray",imgGray)
while True:
        imgHSV=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
        getcontours(imgcanny)
        h_min = cv2.getTrackbarPos("Hue min","trackBars")
        h_max = cv2.getTrackbarPos("Hue max", "trackBars")
        s_min = cv2.getTrackbarPos("Sat min", "trackBars")
        s_max = cv2.getTrackbarPos("Sat max", "trackBars")
        v_min = cv2.getTrackbarPos("Val min", "trackBars")
        v_max = cv2.getTrackbarPos("Val max", "trackBars")
        Blur = cv2.getTrackbarPos("blur", "trackBars")

        print(Blur)
        imgBlur = cv2.GaussianBlur(imgGray, (2*Blur +1, 2*Blur +1), 1)
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])

        mask  = cv2.inRange(imgHSV,lower,upper)
        imgcolor = cv2.bitwise_and(img2, img2, mask=mask)

        stack = np.hstack(( imgGray, imgcanny,imgBlur))
        ##cv2.imshow("1",stack)
        cv2.imshow("2",imgcolor)

        k = cv2.waitKey(33)
        if k == 27:  # Esc key to stop
                break

cv2.imwrite("d://Output.bmp",imgcolor)
print("end")