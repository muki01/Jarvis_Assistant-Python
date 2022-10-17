import cv2
from cvzone.HandTrackingModule import HandDetector

cam = "rtsp://192.168.0.92:554/user=admin&password=halil1978&channel=8&stream=0"
cam2 = "http://admin:123456@192.168.0.234/cgi-bin/sf.cgi"
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)
fingers1= [0,0,0,0,0]
fingers2= [0,0,0,0,0]
fingers = 0
def cntFingers():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    fingers1= [0,0,0,0,0]
    fingers2= [0,0,0,0,0]

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)

    fingers = fingers1[0] + fingers1[1]+fingers1[2]+fingers1[3]+fingers1[4]+fingers2[0] + fingers2[1]+fingers2[2]+fingers2[3]+fingers2[4]
    print(fingers)
    cv2.imshow("Cam", img)
    return fingers