import streamlit as st
import pickle
import pandas as pd
import requests

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #E50914;
        margin-bottom: 20px;
    }
    .movie-card {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# ------------------ POSTER FUNCTION ------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fd19b8606fb25aa22d2a7462256102b6&language=en-US"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return None

    except:
        return None

# ------------------ RECOMMEND FUNCTION ------------------
def recommend(movie):
    movie_index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ------------------ UI ------------------
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend 🎯"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown('<div class="movie-card">', unsafe_allow_html=True)

            if posters[i]:
                st.image(posters[i])
            else:
                st.write("🚫 No Poster")

            st.write(f"**{names[i]}**")
            st.markdown('</div>', unsafe_allow_html=True)