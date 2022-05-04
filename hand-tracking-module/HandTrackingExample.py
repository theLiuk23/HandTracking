import time
import mediapipe as mp
import cv2
import HandTracking as htm

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, drawBool)
    lmList = detector.findPosition(img, drawBool)

    if len(lmList) != 0:
        print(lmList[0])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (5, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()