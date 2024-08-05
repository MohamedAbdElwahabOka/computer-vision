import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)
    # Define the hue ranges and corresponding colors
    hue_ranges = [
    (5, "RED"),
    (15, "ORANGE"),
    (33, "YELLOW"),
    (78, "GREEN"),
    (131, "BLUE"),
    (170, "VIOLET"),
    (180, "RED")  # Assuming hue values can go up to 180 in HSV
]

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
   # Determine the color based on the hue value
    color = "Undefined"
    for upper_limit, hue_color in hue_ranges:
        if hue_value < upper_limit:
            color = hue_color
            break
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    #out.write(frame) #save your video
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()    