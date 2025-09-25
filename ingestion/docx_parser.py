import docx

def parse_docx(file_path: str) -> str:
    """
    extracts text from a DOCX file using python-docx
    
    args:
        file_path (str): path to the DOCX file
    
    returns:
        str: extracted text as a single string
    """
    doc = docx.Document(file_path)
    text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(text).strip()