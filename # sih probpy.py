# ela_detector.py
import cv2
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

def convert_to_ela_image(path, quality=90):
    original = Image.open(path).convert('RGB')
    resaved_name = 'temp_resaved.jpg'
    original.save(resaved_name, 'JPEG', quality=quality)
    resaved = Image.open(resaved_name)
    
    # Calculate difference between original and resaved image
    ela_image = ImageChops.difference(original, resaved)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    return ela_image # Returns high-contrast difference map