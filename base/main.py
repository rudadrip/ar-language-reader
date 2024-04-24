from imageToSpeech import *
from preprocessing import * 

print("Image --> Speech")
print("File Name: ", end="")
fileName = input().strip()
newFileName = convertImage (fileName)
words = grabImageText(newFileName, "ben")
textToSpeech(words, "example", "bn", False)