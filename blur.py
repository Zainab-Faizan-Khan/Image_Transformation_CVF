from PIL import Image, ImageFilter
from flask import current_app
import os,io

def blur_image(image):
    im = Image.open(image)
    im = im.filter(ImageFilter.GaussianBlur(radius=10))
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

def convert_to_grayscale(image):
    im = Image.open(image).convert('L')
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)
    

