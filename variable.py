import cv2, os
path = os.path.dirname(__file__)
def center(text, font, scale,  font_type):
    return cv2.getTextSize(text, font, scale, font_type)
WAJAH = center("Wajah", cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0][0]/2
MATA  = center("Mata", cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0][0]/2