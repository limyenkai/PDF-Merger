from  PyPDF2 import PdfWriter
import sys
import os 

merger = PdfWriter()
current_dir = os.curdir
combined_dir = os.path.join(current_dir, 'Input Files')
output_path = os.path.join(current_dir, 'Output File', 'CombinedPDF.pdf')    

print(combined_dir)

for file in os.listdir(combined_dir): 
    if file.endswith(".pdf"):
        file_path = os.path.join(combined_dir, file)
        merger.append(file_path)

merger.write(output_path)