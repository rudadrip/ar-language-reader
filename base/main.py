from imageToSpeech import *
from preprocessing import * 
from pygame import mixer

print("Image --> Speech")
print("File Name: ", end="")
fileName = input().strip()
newFileName = convertImage (fileName)
words = grabImageText(newFileName, "ben")
textToSpeech(words, "example", "bn", False)

import easyocr
reader = easyocr.Reader(['bn','en']) # this needs to run only once to load the model into memory
result = reader.readtext('example.jpg')
print(result)
total = ""
for x in result:
  print(x[1])
  total+=x[1]+" "
textToSpeech(total, "exampleEASYOCR", "bn", False)
textToSpeech("পথের দেবতা প্রসন্ন হাসিয়া বলেন-মূর্খ বালক পথ তো ঠ্যাঙাড়ে আমার শেষ হয়নি তোমাদের গ্রামে; বাঁশের বনে, বীরু রায়়ের বটতলায় কি ধলচিতের খেয়াঘাটের সীমানায় তোমাদের সোনাডাঙা মাঠ ছাড়িয়ে ইচ্ছামতী পার হয়ে বিলের পাশ কাটিয়া বৈত্রবতীর মধূখালি পদ্মফুলে ভরা খেয়ায় পাড়ি দিয়ে) পথ আমার চলে গেল সামনে, সামনে দেশ ছেড়ে দেশান্তরের দিকে) সূর্যোদয় ছেড়ে শুধুই সামনে জানার গল্ডী এডিয়ে অপরিচয়ের উদ্দেশে সূর্যাস্তের দিকে", "exampleJAIDED" , "bn", False)