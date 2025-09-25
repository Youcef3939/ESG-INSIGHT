import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def get_csv_download_link(df, filename="export.csv"):
    """
    Generate a link to download the given DataFrame as a CSV.
    """
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    b64 = base64.b64encode(csv_buffer.getvalue().encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV</a>'
    return href

def save_chart_to_buffer(plt, filename="chart.png"):
    """
    Save the current matplotlib chart to a buffer for download.
    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    return buffer