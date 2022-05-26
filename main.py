import HandTrackingModule as htm
import cv2
import time

wCam, hCam = 640, 480

detector = htm.handDetector(detectionCon=0.75)
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


ptime = 0
ctime = 0
totalFingers = 0


while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList, _ = detector.findPosition(img, draw=False)


    if len(lmList) != 0:

        fingers = detector.fingersUp()



        totalFingers = fingers.count(1)

        
    else:

        totalFingers = 0



    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.putText(img, f'Finger: {totalFingers}',(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
