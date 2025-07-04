from pypdf import PdfReader

def read_pdf(pdf_document):
    reader = PdfReader(pdf_document)
    full_text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        full_text += page.extract_text()

def read_images():
    pass

print('ok')