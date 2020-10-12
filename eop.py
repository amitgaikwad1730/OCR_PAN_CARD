
"""  Install  pytesseract from https://digi.bib.uni-mannheim.de/tesseract/
    Download the file of v4---  tesseract-ocr-w32-setup-v4.1.0.20190314.exe   """
import pytesseract

""" Install  Opencv by using the pip command """
import cv2
import numpy as np
import re
#%%

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'

#%%

"""Create function  image_to_ocr """
def image_to_ocr(path_of_image,file_name):

    """Reading image using Cv2 and converted to GrayScale Image"""
    img = cv2.imread(path_of_image+file_name,0)

    """Image pre-processing for Image enhancement and Noise Removal if necessary """

    #blur = cv2.medianBlur(img, 5)
    #kernel = np.ones((1, 1), np.uint8)
    #dilate =  cv2.dilate(img, kernel, iterations=5)
    #erode = cv2.erode(dilate, kernel, iterations=5)
    #img = cv2.threshold(cv2.GaussianBlur(img, (3, 3), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    """Writing Preprocees Image to the path"""
    cv2.imwrite(path_of_image+'output'+file_name+'.jpg', img)
    """Converting Image to Text using OCR """
    text = pytesseract.image_to_string(img)
    """ Writing the Output Text to Text File"""
    textfile = open(path_of_image+file_name+'.txt', 'w')
    textfile.write(text)
    textfile.close()
    return text



text = image_to_ocr("C:\\Users\\Amit\\Desktop\\ocr_Assessement\\pan_data\\",'pan.jpg')
"""Text PreProcessing for checking the Document"""
text = text.lower()
text = re.sub("\s\n", '\n', text)
text = re.sub('\n\s+', '\n', text)
text = re.sub("\s\s+", ' ', text)
text = re.sub("\n", ' ', text)
if bool(re.search('permanent account number', text)) == True:
    print("This is PAN Card")
else:
    print("Not PAN Card")





