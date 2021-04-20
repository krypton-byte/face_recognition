import os
from cv2 import CascadeClassifier
from variable import path
FACE = CascadeClassifier(f'{path}/haarcascade/haarcascade_frontalface_default.xml')
EYE = CascadeClassifier(f"{path}/haarcascade/haarcascade_eye.xml")
MOUTH = CascadeClassifier(f"{path}/haarcascade/mouth.xml")