import PyPDF2


pdfiles = ["C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Pdf Merger\\1.pdf.pdf", "C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Pdf Merger\\2.pdf.pdf" , "C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Pdf Merger\\sample.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles :
    pdfFile = open(filename , 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
#merger.write('merged.pdf') #this line was saving the file in Python Projects folder as well 
output_path = "C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Pdf Merger\\merged.pdf"
merger.write(output_path)
print(f"PDFs merged successfully! Output saved at: {output_path}")