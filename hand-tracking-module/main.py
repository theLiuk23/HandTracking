import time
import mediapipe as mp
import cv2

# https://www.youtube.com/watch?v=NZde8Xt78Iw&t=0s&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
# minuto 8:40

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
fps = 30
i = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm, in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                # if id == 0:
                    # cv2.circle(img, (cx,cy), 5, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    i += 1
    if i >= 5:
        cTime = time.time()
        fps = 1 / (cTime - pTime) * 5
        pTime = cTime
        i = 0

    cv2.putText(img, str(int(fps)), (5, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break
    if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()