def text2PDF(file_path,pdf_name):

    from fpdf import FPDF

    pdf = FPDF()
    pdf.set_font("Times")

    #Reading the contents of the file
    with open(file=file_path, mode="r") as file:
        content = file.read()

    pdf.add_page()
    pdf.write(text=str(content))

    pdf.output(f"{pdf_name}.pdf")

