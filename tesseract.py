from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/AppData/Local/Programs/Tesseract-OCR/tesseract'

# Open an image using PIL
image = Image.open(r'data\Spam-Classifier-Performance.PNG')

# Use tesseract to extract text from the image
try:
    text = pytesseract.image_to_string(image)
    print(text)
except Exception as e:
    print(f"An error occured {e}")


