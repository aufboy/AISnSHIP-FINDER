import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def finder(path):
    img = Image.open(path)
    #file_name = img.filename
    #file_name = file_name.split(".")[0]
    
    text = pytesseract.image_to_string(img, lang='eng').strip()
    return str(text)
