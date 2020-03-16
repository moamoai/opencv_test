import cv2
print(cv2.__version__)
print(cv2.__file__)

import os
print(os.path.join(cv2.OPENCV_DATA_DIR, "haarcascades", "haarcascade_frontalface_default.xml"))