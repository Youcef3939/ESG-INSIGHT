import os
import json
import csv

output_dir = os.path.join("data", "output")
csv_path = os.path.join(output_dir, "esg_summary.csv") 

rows = []

for fname in os.listdir(output_dir):
    if fname.endswith(".json"):
        fpath = os.path.join(output_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for sentence_data in data:
                entities_str = "; ".join([f"{e['entity']}: {e['value']}{e['unit'] or ''}" for e in sentence_data.get("entities", [])])
                
                rows.append({
                    "report_name": fname.replace(".json", ""),
                    "sentence": sentence_data.get("sentence", ""),
                    "category": ", ".join(sentence_data.get("category", [])),
                    "entities": entities_str,
                    "greenwashing": sentence_data.get("greenwashing", False)
                })

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["report_name", "sentence", "category", "entities", "greenwashing"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ ESG summary CSV created at: {csv_path}")