from .pdf_parser import parse_pdf
from .docx_parser import parse_docx
from .html_parser import parse_html
from .ocr_parser import parse_scanned_pdf

__all__ = [
    "parse_pdf",
    "parse_docx",
    "parse_html",
    "parse_scanned_pdf"
]