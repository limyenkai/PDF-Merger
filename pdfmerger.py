from  PyPDF2 import PdfWriter
import sys
import os 

merger = PdfWriter()
current_dir = os.curdir
combined_dir = os.path.join(current_dir, 'Input Files')

print(combined_dir)

for file in os.listdir(combined_dir): 
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("Output File/CombinedPDF.pdf")
