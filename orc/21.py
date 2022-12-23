from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy
import os

ocr = PaddleOCR(use_angle_cls=True, lang='en')

image_dir = r"E:/code_retrival/venv/images/"

# =============================================================================
# img_path = image_dir+ "11.png"
# img = Image.open(img_path)
# if img.height < 800: 
#     box = (504, 317, 504 + 270, 317 + 40)
# else: 
#     box = (628, 407, 628 + 360, 407 + 50)
# crop = img.crop(box)
# pic = numpy.array(crop)
# print(type(pic))
# result = ocr.ocr(pic, det=True)
# 
# txts = [line[1][0] for line in result]
# print(txts[0])
# 
# 
# 
# =============================================================================

f = open(r"E:/code_retrival/venv/code.txt", 'w')

#
for root, dirs, file_names in os.walk(image_dir):
        # Iterate over each file_name in the folder
    for file_name in file_names:
            # Open image with PIL
        img = Image.open(image_dir + file_name)
            # Extract text from image
        if img.height < 800:
            box = (504, 317, 504 + 270, 317 + 40)
        else:
            box = (628, 407, 628 + 360, 407 + 50)
        crop = img.crop(box)
        pic = numpy.array(crop)
        result = ocr.ocr(pic, det=True)
        txts = [line[1][0] for line in result]
        text= txts[0]
        #text = (text[:16]) if len(text) > 16 else text
        print(text)
        f.write(text + '\n')
f.close()
#
# =============================================================================
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')
# 
# =============================================================================
