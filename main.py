import os
import easyocr
from pdf2image import convert_from_path
import numpy as np
from enum import Enum



READER = easyocr.Reader(['en']) # this needs to run only once to load the model into memory


class DocumentType(Enum):
    Specification = 1
    Email = 2
    Advertisement = 3
    Handwritten = 4
    Scientific_Report = 5
    Budget = 6
    Scientific_Publication = 7
    Presentation = 8
    File_Folder = 9
    Memo = 10
    Resume = 11
    Invoice = 12
    Letter = 13
    Questionnaire = 14
    Form = 15
    News_Article = 16


print(DocumentType.Specification)
print(DocumentType.News_Article.value)
print(DocumentType.News_Article)


def pdf_or_image(file_path):
    valid_image_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext in valid_image_exts:
        return "image"
    elif file_ext == '.pdf':
        return "pdf"

    raise ValueError(f"Unsupported file format: '{file_ext}'. Only images and PDFs are allowed.")


path_img = "documents/the human brain image.png"
path_pdf = "Caetano CV.pdf"

def read_image(file_path):
    text = READER.readtext(file_path, detail = 0)
    return text


def read_pdf(file_path):
    pages = convert_from_path(file_path, dpi=300, poppler_path='C:/Users/caetano/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin')

    text = ""
    for i, page in enumerate(pages):

        text +=  "\n".join(READER.readtext(np.array(page), detail=0)) + "\n"

    return text

path = path_pdf



def pre_proccess_text(text):
    pass


if pdf_or_image(path) == 'image':
    raw_text = read_image(path)
    print(raw_text)

if pdf_or_image(path) == 'pdf':
    t = read_pdf(path)
    print(t)