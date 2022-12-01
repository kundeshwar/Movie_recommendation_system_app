import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open('movie.pkl', "rb"))
movie_list_1 = pd.DataFrame(movie_dict)
print(st.title('MOVIE RECOMMENDER SYSTEM'))
options = st.selectbox("THIS IS YOUR INTERSTED MOVIE", movie_list_1["title"].values)
print(options)
similar_1 = pickle.load(open("similar_1.pkl","rb"))
similar = pd.DataFrame(similar_1)


def fetch_poster(movie_id):
    a =requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = a.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movie_list_1[movie_list_1['title']==movie].index[0]
    distances = similar[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:11]
    recommended_movie = []
    recommended_poster = []
    for i in movie_list:
        movie_id_1 = movie_list_1.iloc[i[0]].movie_id
        recommended_movie.append(movie_list_1.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id_1))
    return recommended_movie, recommended_poster

if st.button("Recommend"):
    names, poster = recommend(options)
    col1, col2, col3,  col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image(poster[6])
    with col8:
        st.text(names[7])
        st.image(poster[7])
    with col9:
        st.text(names[8])
        st.image(poster[8])
    with col10:
        st.text(names[9])
        st.image(poster[9])
    