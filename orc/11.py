
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   

image_dir = "E:\\code_retrival\\venv\\"
path_to_image = image_dir+'11.png'


im=Image.open(path_to_image)

##print(pytesseract.image_to_string(im,lang='eng'))
if im.height < 800:
    box = (504, 317, 504+270, 317+40)
else:
    box = (628, 407, 628+360, 407+40)
    
crop = im.crop(box)
crop.show()
text = pytesseract.image_to_string(crop,lang='eng')
print(len(text),text)
text = (text[:16]) if len(text) > 16 else text

print(text)
