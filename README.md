# 🎬 Movie Recommender System

A content-based movie recommendation system built using Machine Learning and Streamlit.

## 🚀 Features
- Recommend similar movies based on user selection
- Uses content-based filtering (cosine similarity)
- Displays movie posters using TMDB API
- Interactive UI built with Streamlit

## 🧠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- TMDB API

## 📊 Dataset
- TMDB 5000 Movies Dataset

## ⚙️ How it Works
1. Preprocess movie data (genres, keywords, cast, crew)
2. Create tags and convert text into vectors using CountVectorizer
3. Compute similarity using cosine similarity
4. Recommend top 5 similar movies

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
