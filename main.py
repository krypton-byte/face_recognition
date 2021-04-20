from io import BytesIO
import cv2
import asyncio
import numpy as np
from PIL import Image
from utils import patternResCustom
from partictle import (
    x_partictle as X_ICON,
    love_partictle as LOVE_ICON
)
from variable import (
    WAJAH, MATA
)
from haarcascade import (
    FACE, MOUTH, EYE
)
async def kamera():
    camera = cv2.VideoCapture("example.mp4")
    #image=[]
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = FACE.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=15
        )
        eyes = EYE.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=15
        )
        """mouth = MOUTH.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=20
        )"""
        for (x, y, w, h) in faces:
            frame = Image.fromarray(frame)
            frame.paste(LOVE_ICON, (x, y-70), LOVE_ICON.convert("RGBA"))
            frame = np.array(frame)
            #face=cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #print(center("Wajah", cv2.FONT_HERSHEY_SIMPLEX, 1, 2))
            #frame = cv2.putText(face,"Wajah", (int((x+w/2)-WAJAH), y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        for (x, y, w, h) in eyes:
            frame=Image.fromarray(frame) #eyes=cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            frame.paste(X_ICON, (x, y), X_ICON.convert("RGBA"))
            frame = np.array(frame)
            #print(center("Wajah", cv2.FONT_HERSHEY_SIMPLEX, 1, 2))
            #frame = cv2.putText(eyes,"Mata", (int((x+w/2)-MATA), y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Kamera", frame)
        image.append(Image.fromarray(frame).convert("RGBA"))
        if cv2.waitKey(16) & 0xFF == ord("q"):
            break
        
    print("saving")
    #image[0].save("hasil.webp", quality=60, duration=20, append_images=image[1:], save_all=True)
asyncio.run(kamera())
