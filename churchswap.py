"""
ChurchSwap: Real-time webcam feed with basic controls.
Press 'q' to exit the application.
"""
# pylint: disable=no-member
# run script:python churchswap.py

import cv2
import numpy as np
from ultralytics import YOLO
import logging

logging.getLogger('ultralytics').setLevel(logging.ERROR)

podium = np.array([300, 200, 600, 500])
podium_x_min = podium[0]  # 300
podium_x_max = podium[2]  # 600

persontrackingmodel = YOLO("yolov8s.pt")
metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = metime.read()
    results = persontrackingmodel.track(source=frame, verbose=False)

    person_in_podium = False
    for box in results[0].boxes:
        if int(box.cls) == 0:
            x1, y1, x2, y2 = box.xyxy[0]
            center_x = (x1 + x2) / 2

            if podium[0] < center_x < podium[2]:
                person_in_podium = True
    print(f"Boxes detected: {len(results[0].boxes)}")  # Add
    annotated_frame = results[0].plot()

    if not ret:
        break

    cv2.imshow('Churchswap', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

metime.release()
cv2.destroyAllWindows()
