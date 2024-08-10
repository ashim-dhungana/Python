from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

path = "/run/media/ashim/Programming/Python/CWH Course/Module/files"
content = os.listdir(path)

files = [file for file in content if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()