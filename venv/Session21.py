import cv2
import pytesseract

im = cv2.imread("computervision.jpg", cv2.IMREAD_COLOR)

# Run tesseract OCR on image
text = pytesseract.image_to_string(im, lang='eng')

# Print recognized text
print(text)