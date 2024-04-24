from gtts import gTTS
from PIL import Image
import pytesseract
import os

def textToSpeech (msg, fileName, language, isSlow):
  outputFile = gTTS(text=msg, lang=language, slow=isSlow)
  outputFile.save(fr"{fileName}.mp3") 

def grabImageText (image, language):
  pytesseract.pytesseract.tesseract_cmd = '../Tesseract-OCR/tesseract.exe'
  text = pytesseract.image_to_string(Image.open(image), lang=language, config='--psm 11') #"ben"
  print(text)
  return text

def convertImage (image):
  image=str(image)
  splittage = image.split(".")
  if (splittage[1]=="jpg"):
    im = Image.open(image)
    im.save(f"{splittage[0].strip()}.png")
  return f"{splittage[0].strip()}.png"

print(grabImageText("example.png","ben"))