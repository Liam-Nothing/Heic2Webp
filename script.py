from pathlib import Path
from PIL import Image
from heic2png import HEIC2PNG
import os
import sys

def convert_to_webp(source):
    if not os.path.exists(user_path + "/output"):
        os.makedirs(user_path + "/output")
    destination_path = Path(os.path.dirname(source) + "/output/" + os.path.basename(source))
    destination = destination_path.with_suffix(".webp")
    image = Image.open(source)
    image.save(destination, format="webp")
    return destination


def main():
    paths = Path(user_path).glob("**/*.heic")
    for path in paths:
        heic_img = HEIC2PNG(path)
        png_path = heic_img.save()
        webp_path = convert_to_webp(png_path)
        os.remove(png_path)
        print(webp_path)
try:
    user_path = sys.argv[1]
    main()
except:
    print("Error, syntax: py script.py C:\\Users\\you\\Desktop\\images")
    exit