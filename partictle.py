print("LOAD PARTICTLE DATA")
import os
from utils import patternResCustom
from PIL import Image
from variable import path
x_partictle = Image.open(f"{path}/assets/x.png").resize((50, 50))
love_partictle = Image.open(f"{path}/assets/love_icon.png").resize(tuple(patternResCustom(Image.open(f"{path}/assets/love_icon.png"), res=200)))