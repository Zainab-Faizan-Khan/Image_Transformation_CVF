from email.mime import image
import PIL
from PIL import Image, ImageFilter,ImageEnhance, ImageDraw
from flask import current_app
import os,io
import numpy as np
import imageio
import scipy.ndimage
import cv2
def blur_image(image):
    im = Image.open(image)
    im = im.filter(ImageFilter.GaussianBlur(radius=7))
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

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8') 

def sketchimage(image):
    s=imageio.imread(image)
    print("1")
    g=convert_to_grayscale(s)
    print("2")
    i=255-g
    print("3")
    b=scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    print("4")
    r=dodge(b,g)
    print("5")
    cv2.imwrite("PNG",r)
    

def sharpen_image(image):
    im = Image.open(image)
    enhancer =  ImageEnhance.Sharpness(im)
    im= enhancer.enhance(6)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)
   
def contrast_image(image):
    im = Image.open(image)
    enhancer = ImageEnhance.Contrast(im)
    im= enhancer.enhance(1.6)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

def dull_image(image):
    im = Image.open(image)
    enhancer = ImageEnhance.Contrast(im)
    im= enhancer.enhance(0.3)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

def transpose_image(image):
    im = Image.open(image)
    out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)


