import os
import json

OUTPUT_DIR = os.path.join("data", "output")  

def compute_risk_for_report(report_json_path):
    """Compute greenwashing risk for a single report."""
    with open(report_json_path, "r", encoding="utf-8") as f:
        sentences = json.load(f)
    
    total_sentences = len(sentences)
    if total_sentences == 0:
        return 0.0  
    
    flagged_sentences = sum(1 for s in sentences if s.get("greenwashing", False))

    risk_score = (flagged_sentences / total_sentences) * 100
    return round(risk_score, 2)

def compute_risk_all_reports(output_dir=OUTPUT_DIR):
    """Compute greenwashing risk for all reports in output_dir."""
    results = []
    for fname in os.listdir(output_dir):
        if fname.endswith(".json"):
            fpath = os.path.join(output_dir, fname)
            risk = compute_risk_for_report(fpath)
            results.append({
                "report_name": fname.replace(".json", ""),
                "risk_score": risk
            })
    return results

if __name__ == "__main__":
    all_risks = compute_risk_all_reports()
    for r in all_risks:
        print(r)