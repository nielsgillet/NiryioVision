lower_black = np.array([0, 0, 0])
upper_black = np.array([35, 35, 35])
mask = cv2.inRange(hsv, lower_black, upper_black)