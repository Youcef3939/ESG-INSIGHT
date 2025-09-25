import os
from ingestion import parse_pdf, parse_docx, parse_html, parse_scanned_pdf

SUPPORTED_FORMATS = [".pdf", ".docx", ".html", ".htm"]

def load_document(file_path: str) -> str:
    """
    loads and extracts text from a given document
    supports PDF, scanned PDF, DOCX, and HTML files

    args:
        file_path (str): path to the file

    returns:
        str: extracted text
    """
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        text = parse_pdf(file_path)
        if not text.strip():  
            text = parse_scanned_pdf(file_path)
        return text

    elif ext == ".docx":
        return parse_docx(file_path)

    elif ext in [".html", ".htm"]:
        return parse_html(file_path)

    else:
        raise ValueError(f"unsupported file format: {ext}")
    
if __name__ == "__main__":
    for f in ["data/reports/sample.pdf", 
              "data/reports/sample.docx", 
              "data/reports/sample.html"]:
        print(f"\n {f}")
        text = load_document(f)
        print(text[:300])  