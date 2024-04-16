from imageToSpeech import *

convertImage ("example.jpg")
words = grabImageText("example.png", "ben")
textToSpeech(words, "example", "bn", False)