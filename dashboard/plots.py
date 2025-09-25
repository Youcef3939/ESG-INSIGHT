import matplotlib.pyplot as plt
import streamlit as st

def plot_pillar_compliance(df):
    pillars = ["Environmental", "Social", "Governance"]
    df_plot = df.set_index("report_name")[pillars]
    ax = df_plot.plot(kind="bar", stacked=True, figsize=(10, 4), colormap="tab20c")
    plt.ylabel("Compliance %")
    plt.title("Compliance by Pillar per Report")
    plt.xticks(rotation=45)
    plt.legend(title="Pillar")
    st.pyplot(plt.gcf())
    plt.clf()

def plot_benchmark_ranking(df):
    df_plot = df.sort_values("benchmark_score", ascending=False)
    ax = df_plot.plot(
        x="report_name",
        y="benchmark_score",
        kind="barh",
        figsize=(10, 4),
        color="skyblue"
    )
    plt.xlabel("Benchmark Score")
    plt.title("Overall ESG Benchmark Ranking")
    st.pyplot(plt.gcf())
    plt.clf()