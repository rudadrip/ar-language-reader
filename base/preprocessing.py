import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize (img):
  image = cv2.imread(img)
  smaller = cv2.resize(image, (0, 0), fx = 0.33, fy = 0.33)
  cv2.imshow('Resized',smaller)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def deskew(img):
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_gray = cv2.bitwise_not(img_gray)

  thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  coords = np.column_stack(np.where(thresh > 0))
  angle = cv2.minAreaRect(coords)[-1] 
    
  if (angle < 0 and angle >= -10):
      angle = -angle #this was intended to undo skew for values in [-10, 0) by simply rotating using the opposite sign
  else:
      angle = (90 + angle)/2  
    
  (h, w) = img.shape[:2]
  center = (w // 2, h // 2)
  
  M = cv2.getRotationMatrix2D(center, angle, 1.0)
  deskewed = cv2.warpAffine(img, M, (w, h), flags = cv2.INTER_CUBIC, borderMode = cv2.BORDER_REPLICATE)

def thresholding (image):
  image1 = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
  image1 = cv2.imread(image)
  cv2.imshow('OG', image)
  img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) 
  cv2.imshow('Post', thresh1)
  if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  

resize("example.jpg")
