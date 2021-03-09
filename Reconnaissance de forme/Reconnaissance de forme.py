import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2RGB)
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([170, 80, 80])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if area > 2000:
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            if len(approx) == 12:
                cv2.putText(frame, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len(approx) == 4:
                cv2.putText(frame, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len(approx) == 8:
                cv2.putText(frame, "Round", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(27)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
