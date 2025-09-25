import os
import json
import pandas as pd

OUTPUT_DIR = os.path.join("data", "output")  
TAXONOMY_CSV = os.path.join("data", "taxonomy", "sample.csv")

def load_taxonomy(csv_path=TAXONOMY_CSV):
    """Load taxonomy rules from CSV."""
    return pd.read_csv(csv_path)

def score_report(report_json_path, taxonomy_df):
    """Compute compliance score for a single report."""
    with open(report_json_path, "r", encoding="utf-8") as f:
        sentences = json.load(f)
    
    pillars = taxonomy_df["category"].unique()
    pillar_scores = {p: {"matched": 0, "total": 0} for p in pillars}

    for sentence_data in sentences:
        categories = sentence_data.get("category", [])
        sentence_text = sentence_data.get("sentence", "").lower()

        for cat in categories:
            cat_rules = taxonomy_df[taxonomy_df["category"] == cat]
            pillar_scores[cat]["total"] += len(cat_rules)

            matched = sum(1 for keyword in cat_rules["keyword"] if keyword.lower() in sentence_text)
            pillar_scores[cat]["matched"] += matched

    final_scores = {}
    for cat, vals in pillar_scores.items():
        total = vals["total"]
        matched = vals["matched"]
        score = (matched / total * 100) if total > 0 else 100
        final_scores[cat] = round(score, 2)

    overall_score = round(sum(final_scores.values()) / len(final_scores), 2) if final_scores else 100

    return {
        "report_name": os.path.basename(report_json_path).replace(".json", ""),
        "compliance_score": overall_score,
        "pillar_scores": final_scores
    }

def score_all_reports(output_dir=OUTPUT_DIR, taxonomy_csv=TAXONOMY_CSV):
    """Compute compliance scores for all NLP outputs."""
    taxonomy_df = load_taxonomy(taxonomy_csv)
    results = []

    for fname in os.listdir(output_dir):
        if fname.endswith(".json"):
            fpath = os.path.join(output_dir, fname)
            report_score = score_report(fpath, taxonomy_df)
            results.append(report_score)
    
    return results

if __name__ == "__main__":
    scores = score_all_reports()
    for s in scores:
        print(s)