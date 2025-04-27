from fpdf import FPDF

file=input("Enter file name")
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)
f=open(file,"r")
for x in f:
    pdf.cell(500,10,txt=x,ln=1,align='J')
pdf.output("C:\\Users\\Vijay\\OneDrive\\Desktop\\filepdf.pdf")
if("filepdf.pdf"):
    print("pdf created as filepdf.pdf in C:\\Users\\Vijay\\OneDrive\\Desktop")
