import os
from fpdf import FPDF

def text2PDF(file_path,pdf_name):

    pdf = FPDF()
    pdf.add_font(family="ARIAL", fname="D:/Sushrutha/Projects/PDF_APP/fonts/arial.TTF")
    pdf.set_font(family="ARIAL")
    

    #Reading the contents of the file
    with open(file=file_path, mode="r") as file:
        content = file.read()

    pdf.add_page()
    pdf.write(text=str(content))

    file_path=os.path.dirname(file_path)

    pdf.output(f"{file_path}/{pdf_name}.pdf")