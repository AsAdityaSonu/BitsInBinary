import os
from pypdf import PdfWriter

def merge_pdfs(input_folder, output_file):
    merger = PdfWriter()
    
    # List all PDF in the folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    
    # Sort files
    pdf_files.sort()

    # add PDFs to the merger
    for pdf in pdf_files:
        merger.append(os.path.join(input_folder, pdf))
    
    # Write the merged PDF
    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    input_folder = "2_PDF_Merge/PDFs"
    output_file = "2_PDF_Merge/OUTPUT/merged.pdf"
    merge_pdfs(input_folder, output_file)