## Import the PDF reading tool we installed earlier
from pypdf import PdfReader
#A function that takes a file path like "uploads/document.pdf"
def extract_text(pdf_path):
    #Opens the PDF file

    reader = PdfReader(pdf_path)
    #Start with an empty string to collect all text
    text = ""
    #Loop through every page and add its text to the string
    for page in reader.pages:
        text += page.extract_text()
    
    return text