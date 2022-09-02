
from PIL import Image
import os
from pathlib import Path


directory = "img"
for item in os.listdir(directory):
    item = item
    image = Image.open(f"img/{item}")
    image = image.resize((1000,563),Image.ANTIALIAS)
    name = item
    image.save(fp=f"{name}.png")
 
