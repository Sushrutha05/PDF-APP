import tkinter as tk
from tkinter import filedialog
import pdfGenerator as pdf
import os

window = tk.Tk()
window.geometry(("800x500"))
window.title("Text to PDF converter")

def getSourceFile():
    path = filedialog.askopenfilename()
    name = os.path.basename(path)
    name = os.path.splitext(name)[0]
    if not path:
        uploadedFile.config(text='File not selected')
    else:
        uploadedFile.config(text=f'File uploaded is "{path}"')
        generate_button = tk.Button(master=window, text= "GENERATE", command= lambda: pdf.text2PDF(filePath,fileName)).pack()

    global filePath
    global fileName
    
    filePath = path
    fileName = name
    


browse_button = tk.Button(master=window, text= "BROWSE",command=getSourceFile).pack()

uploadedFile = tk.Label(master=window, text="File not uploaded yet")
uploadedFile.pack()



window.mainloop()