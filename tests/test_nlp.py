import os
import json
import csv
import pytest
from nlp import extract_entities, detect_greenwashing, semantic_tag_sentences
from ingestion.loader import load_document

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")

@pytest.mark.parametrize("fname", os.listdir(REPORTS_DIR))
def test_nlp_pipeline(fname):
    fpath = os.path.join(REPORTS_DIR, fname)
    if not os.path.isfile(fpath) or not fpath.lower().endswith((".pdf", ".docx", ".html", ".txt")):
        pytest.skip(f"Skipping non-report file: {fname}")

    text = load_document(fpath)
    assert text.strip() != "", "Document should not be empty"

    tagged_sentences = semantic_tag_sentences(text, threshold=0.3)
    assert isinstance(tagged_sentences, list), "Tagged sentences should be a list"

    for t in tagged_sentences:
        t['entities'] = extract_entities(t['sentence'])
        t = detect_greenwashing(t)
        # Check structure
        assert "sentence" in t
        assert "category" in t
        assert "entities" in t
        assert "greenwashing" in t

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"{fname}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(tagged_sentences, f, ensure_ascii=False, indent=2)
    
    assert os.path.exists(output_path), "Output JSON should exist"

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) > 0, "JSON output should have at least one sentence"
        for s in data:
            assert "sentence" in s
            assert "category" in s
            assert "entities" in s
            assert "greenwashing" in s