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
import PyATEMMax
from time import sleep

switcher = PyATEMMax.ATEMMax()
switcher.connect("192.168.1.111")
switcher.waitForConnection()

logging.getLogger('ultralytics').setLevel(logging.ERROR)

podium = np.array([300, 200, 600, 500])
podium_x_min = podium[0]  # 300
podium_x_max = podium[2]  # 600

persontrackingmodel = YOLO("yolov8s.pt")
metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)

person_in_podium = False

while True:
    ret, frame = metime.read()
    results = persontrackingmodel.track(
        source=frame, verbose=False, classes=[0])

    for box in results[0].boxes:
        human_count = sum(1 for box in results[0].boxes if int(box.cls) == 0)
        if human_count < 1:
            person_in_podium = False
            sleep(2)
            switcher.setProgramInputVideoSource(1, 2)
            break
    annotated_frame = results[0].plot()

    if not ret:
        break

    cv2.imshow('Churchswap', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

metime.release()
cv2.destroyAllWindows()
