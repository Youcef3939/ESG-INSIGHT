import os
import pytest
from ingestion.loader import load_document

SAMPLE_FILES = {
    "pdf": "data/reports/sample.pdf",
    "docx": "data/reports/sample.docx",
    "html": "data/reports/sample.html"
}

@pytest.mark.parametrize("filetype", SAMPLE_FILES.keys())
def test_ingestion(filetype):
    file_path = SAMPLE_FILES[filetype]

    if not os.path.exists(file_path):
        pytest.skip(f"skipping {filetype} test: {file_path} not found.")

    text = load_document(file_path)
    assert isinstance(text, str), "extracted text should be a string"
    assert len(text) > 0, f"{filetype} extraction returned empty text"