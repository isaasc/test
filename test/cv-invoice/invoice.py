import pytesseract
from PIL import Image
import cv2
import os
import re
import base64
import numpy as np
import tempfile

def run_tesseract(filename):
    correct_image = base64.b64decode(filename)
    temp_filename = prepare_image(correct_image)
    text = pytesseract_process(temp_filename)

def prepare_image(image_data):
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_filename = tempfile.mktemp(suffix='.jpg')
    cv2.imwrite(temp_filename, gray)
    return temp_filename

def pytesseract_process(filename):
    text = pytesseract.image_to_string(Image.open(filename), config='--psm 4')
    return text

def easyocr_process(filename):
    reader = easyocr.Reader(['en'], model_storage_directory='./EasyOCR/model/english_g2.pth')
    result = reader.readtext(filename)
    return result

def evaluate_success(text):
    ptr = 'R(?:S|\\$) +(\\d+,\\d{2})'
    reMatch = re.search(ptr, str(text))

    if reMatch:
        result = reMatch.group(1)
        # print("sucesso: " + result)
        return result
    else:
        return None




