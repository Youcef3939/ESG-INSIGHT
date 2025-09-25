import os
import pandas as pd
from scoring import compliance_score, risk_score

OUTPUT_DIR = os.path.join("data", "output")  
EXPORT_CSV = os.path.join("data", "output", "benchmarking_summary.csv")

def benchmark_reports():
    compliance_results = compliance_score.score_all_reports()
    compliance_df = pd.DataFrame(compliance_results)

    risk_results = risk_score.compute_risk_all_reports()
    risk_df = pd.DataFrame(risk_results)

    merged_df = pd.merge(compliance_df, risk_df, on="report_name")

    # higher compliance + lower risk = better rank
    # we'll define benchmark_score = compliance_score - risk_score
    merged_df["benchmark_score"] = merged_df["compliance_score"] - merged_df["risk_score"]

    merged_df["rank"] = merged_df["benchmark_score"].rank(method="min", ascending=False).astype(int)

    merged_df = pd.concat([merged_df.drop("pillar_scores", axis=1),
                           pd.json_normalize(merged_df["pillar_scores"].tolist())], axis=1)

    merged_df.to_csv(EXPORT_CSV, index=False)
    return merged_df

if __name__ == "__main__":
    summary = benchmark_reports()
    print(summary)