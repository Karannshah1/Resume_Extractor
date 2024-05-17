import PyPDF2
import yaml 
import logging
import os
import sys
from common_import import *



def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
    # with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        logger.info(f"Number of pages: {num_pages}")

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    # print(text)
    return text

# path = "C:/Users/91910/OneDrive/Documents/Sem-7/Karan Shah Latest Resume.pdf"
# res = extract_text_from_pdf(path)

if __name__ == "__main__":
    PDF_PATH = SETTINGS['source_pdf_file']
    print(PDF_PATH)
    extracted_text = extract_text_from_pdf(pdf_path=PDF_PATH)
    # print(extracted_text)