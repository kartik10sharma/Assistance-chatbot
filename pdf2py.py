# pdf2py.py

import os
import pdfplumber

def extract_text_from_pdfs(pdf_folder):
    extracted_text = ""
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            with pdfplumber.open(os.path.join(pdf_folder, filename)) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"
    return extracted_text

import re
# cleaning is done here
def clean_text(text):
    # Removing special char and digits
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # lowercase only
    text = text.lower()
    return text



