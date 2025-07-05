import os
import easyocr
from pdf2image import convert_from_path
import numpy as np



READER = easyocr.Reader(['en']) # this needs to run only once to load the model into memory


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



if pdf_or_image(path) == 'image':
    t = read_image(path)
    print(t)

if pdf_or_image(path) == 'pdf':
    t = read_pdf(path)
    print(t)