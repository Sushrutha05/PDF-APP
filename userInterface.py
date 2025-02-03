import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import pdfGenerator as pdf
import os
from PIL import Image

window = ctk.CTk()
window._set_appearance_mode('dark')
window.geometry("800x500")
window.title("Text to PDF converter")
window.resizable(False, False)

selectedTheme = True  # Initial theme set to dark

image1=ctk.CTkImage(light_image=Image.open("D:/Sushrutha/Projects/PDF_APP/moon.png"))
image2=ctk.CTkImage(light_image=Image.open("D:/Sushrutha/Projects/PDF_APP/sun.png"))

selectedImage = 'Image1'

def switchTheme():
    global selectedTheme
    global selectedImage

    if selectedTheme:  # If True, switch to light theme
        selectedTheme = False
        selectedImage = 'Image2'
        window._set_appearance_mode('light')
        uploadedFile.configure(text_color='black', bg_color='#EBEBEB')
        theme_button.configure(image = image2, text_color= 'black', fg_color = '#EBEBEB', background_corner_colors=('#EBEBEB', '#EBEBEB', '#EBEBEB', '#EBEBEB'), hover_color='#EBEBEB')
    else:  # If False, switch to dark theme
        selectedTheme = True
        selectedImage = 'Image1'
        window._set_appearance_mode('dark')
        uploadedFile.configure(text_color='white', bg_color='#242424')
        theme_button.configure(image = image1, text_color = 'white', fg_color = '#242424', background_corner_colors=('#242424', '#242424', '#242424', '#242424'),hover_color='#242424')

def getSourceFile():
    path = filedialog.askopenfilename()
    name = os.path.basename(path)
    name = os.path.splitext(name)[0]
    if not path:
        uploadedFile.configure(text='File not selected')
    else:
        uploadedFile.configure(text=f'File uploaded is "{path}"')
        uploadedFile.place(relx = 0.25)

        generate_button = ctk.CTkButton(master=window, text="GENERATE", command=lambda: pdf.text2PDF(filePath, fileName))
        generate_button.place(relx= 0.445, rely=0.5)

    global filePath
    global fileName
    
    filePath = path
    fileName = name

browse_button = ctk.CTkButton(master=window, text="BROWSE", command=getSourceFile).place(relx=0.45, rely=0.2)

theme_button = ctk.CTkButton(master=window, image=image1, text="", width=0 ,command=switchTheme, bg_color="transparent", fg_color='#242424', background_corner_colors=('#242424', '#242424', '#242424', '#242424'), hover_color='#242424')
theme_button.place(relx=0)

uploadedFile = ctk.CTkLabel(master=window, text="File not uploaded yet")
uploadedFile.place(relx=0.465, rely=0.3)

window.mainloop()

