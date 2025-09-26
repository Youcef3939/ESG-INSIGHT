import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

taxonomy_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "taxonomy", "sample.csv")
taxonomy_df = pd.read_csv(taxonomy_path)

taxonomy_dict = {}
for _, row in taxonomy_df.iterrows():
    cat = row['category'].strip().lower()
    keyword = row['keyword'].strip().lower()
    taxonomy_dict.setdefault(cat, []).append(keyword)

flat_keywords = []
flat_categories = []
for cat, keywords in taxonomy_dict.items():
    for kw in keywords:
        flat_keywords.append(kw)
        flat_categories.append(cat.capitalize())

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def semantic_tag_sentences(text, threshold=0.3):
    """
    tag sentences with ESG categories using semantic similarity
    returns list of dicts: [{'sentence': ..., 'category': [...]}]
    """
    sentences = split_sentences(text)
    tagged = []

    if not sentences:
        return tagged

    vectorizer = TfidfVectorizer()
    all_texts = flat_keywords + sentences
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    keyword_vecs = tfidf_matrix[:len(flat_keywords)] # type: ignore
    sentence_vecs = tfidf_matrix[len(flat_keywords):] # type: ignore

    for idx, s_vec in enumerate(sentence_vecs):
        sims = cosine_similarity(s_vec, keyword_vecs)[0]  
        matched_cats = set()
        for i, score in enumerate(sims):
            if score >= threshold:
                matched_cats.add(flat_categories[i])
        if matched_cats:
            tagged.append({'sentence': sentences[idx], 'category': list(matched_cats)})
    return tagged
