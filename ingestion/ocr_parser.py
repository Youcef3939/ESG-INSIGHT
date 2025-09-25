import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def parse_scanned_pdf(file_path: str) -> str:
    """
    extracts text from scanned PDFs using OCR (Tesseract)
    
    args:
        file_path (str): path to the scanned PDF file
    
    Returns:
        str: extracted text as a single string
    """
    text = ""
    pdf_doc = fitz.open(file_path)
    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        pix = page.get_pixmap() # type: ignore
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples) # type: ignore
        text += pytesseract.image_to_string(img)
    return text.strip()