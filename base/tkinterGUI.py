from imageToSpeech import *
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

win = tk.Tk() 
win.title("Language Script Reader")
win.resizable(False, False)
window_height = 200
window_width = 400
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


l = Label(win, text = "Language Script Reader")
l.config(font =("Courier", 14))

button = tk.Button(win, text='Open', command=UploadAction)

l.pack()
button.pack()

win.mainloop()