from pptx import Presentation
from PIL import Image, ImageEnhance
import pytesseract
from io import BytesIO
import cv2
import numpy as np
import os

def extract_numeric_part(s):
    presentation = Presentation(s)
    if(len(presentation.core_properties.comments.strip()) <=30):
        print(s)
    elif(len(presentation.core_properties.subject.strip()) <= 30):
        print(s)
    
    
for file in os.listdir("D:/Users/yihao zhuo/Desktop/ppt/dir/ppt 16-9"):
   
    if file.endswith(".pptx"):
        pptx_path = f"D:/Users/yihao zhuo/Desktop/ppt/dir/ppt 16-9/{file}"
        extract_numeric_part(pptx_path)
       
