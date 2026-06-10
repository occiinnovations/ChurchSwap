# ChurchSwap

ChurchSwap is a real-time person detection system that automatically manages camera switching during church services. Using YOLOv8 computer vision, it monitors a defined podium area via webcam. When someone is at the podium, the system keeps the focused camera view active. When the podium zone is empty, it automatically switches to a wide-angle camera via ATEM switcher integration. This enables seamless, hands-free camera management for livestreaming without requiring a dedicated operator to manually switch between views.

## Installation
```bash
pip install -r requirements.txt
python churchswap.py
```

## Status
MVP v1 - Detection working, ready for church hardware testing.
