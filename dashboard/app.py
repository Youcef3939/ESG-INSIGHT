import streamlit as st
import pandas as pd
from plots import plot_pillar_compliance, plot_benchmark_ranking
from export import save_chart_to_buffer
import matplotlib.pyplot as plt

CSV_PATH = "data/output/benchmarking_summary.csv"

@st.cache_data
def load_data(path=CSV_PATH):
    return pd.read_csv(path)

df = load_data()

st.set_page_config(page_title="esg insight dashboard", layout="wide")
st.title("🌱 ESG INSIGHT DASHBOARD")

st.sidebar.header("filters & options")
report_filter = st.sidebar.multiselect(
    "select reports to display",
    options=df["report_name"].unique(),
    default=df["report_name"].unique()
)
filtered_df = df[df["report_name"].isin(report_filter)]

st.sidebar.markdown("---")
st.sidebar.subheader("download filtered csv")
st.sidebar.download_button(
    label="download csv",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_reports.csv",
    mime="text/csv"
)

st.subheader("key metrics")
col1, col2, col3 = st.columns(3)
col1.metric("average compliance score", f"{filtered_df['compliance_score'].mean():.2f}")
col2.metric("average risk score", f"{filtered_df['risk_score'].mean():.2f}")
top_report = filtered_df.sort_values("benchmark_score", ascending=False).iloc[0]
col3.metric("top ranked report", f"{top_report['report_name']} ({top_report['benchmark_score']:.2f})")

st.subheader("benchmarking table")
st.dataframe(filtered_df)

st.subheader("pillar compliance")
fig, ax = plt.subplots(figsize=(10,5))
pillars = ["Environmental", "Social", "Governance"]

colors = ["#4CAF50", "#FFC107", "#2196F3"]  

filtered_df.set_index("report_name")[pillars].plot(
    kind="bar",
    stacked=True,
    ax=ax,
    color=colors
)
plt.ylabel("compliance %")
plt.xlabel("report")
plt.title("compliance by pillar per report")
plt.xticks(rotation=45)
plt.legend(title="pillar")
st.pyplot(fig)

buf = save_chart_to_buffer(plt, filename="pillar_compliance.png")
st.download_button(label="download pillar compliance chart", data=buf, file_name="pillar_compliance.png", mime="image/png")
plt.close(fig)

st.subheader("benchmark ranking")
fig, ax = plt.subplots(figsize=(10,5))

filtered_df.sort_values("benchmark_score", ascending=False).plot(
    x="report_name",
    y="benchmark_score",
    kind="barh",
    ax=ax,
    color="#2196F3"
)
plt.xlabel("benchmark score")
plt.ylabel("report")
plt.title("overall esg benchmark ranking")
st.pyplot(fig)

buf = save_chart_to_buffer(plt, filename="benchmark_ranking.png")
st.download_button(label="download benchmark ranking chart", data=buf, file_name="benchmark_ranking.png", mime="image/png")
plt.close(fig)