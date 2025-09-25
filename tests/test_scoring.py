import os
import pytest
from scoring import compliance_score, risk_score, benchmarking

OUTPUT_DIR = os.path.join("data", "output")

@pytest.mark.parametrize("module_func", [
    compliance_score.score_all_reports,
    risk_score.compute_risk_all_reports,
    benchmarking.benchmark_reports
])
def test_scoring_modules(module_func):
    """test that scoring modules run without errors and return expected data types"""
    results = module_func()
    assert isinstance(results, list) or hasattr(results, "to_csv"), \
        f"{module_func.__name__} did not return a list or DataFrame-like object"
    if isinstance(results, list):
        assert all(isinstance(r, dict) for r in results), \
            f"{module_func.__name__} results are not all dicts"
        for r in results:
            assert "report_name" in r, f"{module_func.__name__} missing report_name"
            if "compliance_score" in r:
                assert isinstance(r["compliance_score"], (int, float))
            if "risk_score" in r:
                assert isinstance(r["risk_score"], (int, float))