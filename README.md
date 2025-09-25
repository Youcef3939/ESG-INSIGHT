# ESG insight

an **ai powered ESG compliance monitoring and greenwashing detection**

it's an **end to end python solution, 100% open source, and production ready**

![Python](https://img.shields.io/badge/python-blue)
![Greenwashing Detector](https://img.shields.io/badge/greenwashing-🚫-red)
![Big4 Ready](https://img.shields.io/badge/big4-ready-✨)
![Data Geek](https://img.shields.io/badge/data%20geek-📊-blue)
---

## project overview

**ESG insight** is a fully python based platform that automatically analyzes corporate ESG (environmental, social, and governance) reports to:

- detect potentiel **greenwashing** claims

- assess **compliance with EU taxonomy, CSRD, and SFDR rules**

- score ESG performance per pillar

- generate **auditor ready reports** and visual dashboards

the system is free to run and uses only open-source libraries and public ESG data

---

## key features

1. **end-to-end pipeline**

   - report ingestion (PDF, DOCX, HTML, scanned PDFs)

   - NLP pipeline (keyword detection, entity recognition, greenwashing detection)

   - semantic rule matching (EU Taxonomy / CSRD / SFDR)

   - compliance and risk scoring

   - interactive dashboard & report export

2. **document ingestion**

   - PDF, DOCX, HTML parsing

   - OCR support for scanned documents

   - cleaned, structured text for NLP

3. **NLP & greenwashing detection**

   - detect ESG-related keywords and metrics

   - identify vague or unverified claims

   - semantic matching to regulatory rules using FAISS and sentence embeddings

4. **scoring & benchmarking**

   - compliance score per ESG pillar

   - greenwashing risk score

5. **interactive dashboard**

   - built with streamlit

   - visualizations of ESG scores, flagged claims, and compliance gaps

   - export to excel or PDF for regulators or auditors

---

## workflow

ingestion --> NLP --> scoring --> dashboard

---


## getting started

1. **clone the repo**

```bash

git clone https://github.com/Youcef3939/ESG_Insight.git

cd ESG_Insight 
```

2. **install dependencies**

```
pip install -r requirements.txt
```

3. **add your data**

- place ESG reports in data/reports/

- add EU taxonomy / CSRD / SFDR rules in data/taxonomy/ (JSON format)

4. **run the streamlit dashboard**

```
streamlit run dashboard/app.py
```

5. **upload a report and view compliance results**

- ESG insight will automatically parse, analyze, score, and visualize results

- export auditor ready excel/PDF reports


---

## dashboard visualization
![alt text](<pics/image1.png>) ![alt text](<pics/image2.png>) ![alt text](<pics/image3.png>)

---


## why was **ESG insight** born?

- real world application of **AI in ESG compliance auditing**

- detects **greenwashing** --> demonstrates ethical and financial risk awarness

- **end to end**, fully automated python pipeline

- interactive dashboard + export features

---

if you liked this project, don't hesitate to give it a star 🌟
