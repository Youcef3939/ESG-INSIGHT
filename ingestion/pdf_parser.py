import pdfplumber

def parse_pdf(file_path: str) -> str:
    """
    extracts text from a PDF file using pdfplumber
    
    args:
        file_path (str): path to the PDF file
    
    returns:
        str: extracted text as a single string
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()