import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def image_read():
    img = cv2.imread('img\\temp\\current.png')
    return pytesseract.image_to_string(img)