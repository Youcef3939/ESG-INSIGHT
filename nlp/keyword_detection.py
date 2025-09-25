import os
import json
from ingestion.loader import load_document
from nlp.entity_recognition import extract_entities
from nlp.greenwashing import detect_greenwashing
from nlp.embedding_search import semantic_tag_sentences

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(base_dir, "data", "reports")
    output_dir = os.path.join(base_dir, "data", "output")

    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(reports_dir):
        fpath = os.path.join(reports_dir, fname)
        if os.path.isfile(fpath) and fpath.lower().endswith((".pdf", ".docx", ".html", ".txt")):
            print(f"\n📄 Processing {fname}")
            try:
                text = load_document(fpath)

                tagged_sentences = semantic_tag_sentences(text, threshold=0.3)

                for t in tagged_sentences:
                    t['entities'] = extract_entities(t['sentence'])
                    t = detect_greenwashing(t)

                if not tagged_sentences:
                    print("no ESG keywords or semantic matches found.")
                else:
                    output_path = os.path.join(output_dir, f"{fname}.json")
                    with open(output_path, "w", encoding="utf-8") as f:
                        json.dump(tagged_sentences, f, ensure_ascii=False, indent=2)
                    print(f"exported results to {output_path}")

            except Exception as e:
                print(f"failed to process {fname}: {e}")