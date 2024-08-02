import streamlit as st
import pandas as pd
from scrape import get_image_from_imdb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit.components.v1 as components


st.set_page_config(layout='wide', page_title='Miuul Movie Recommender')


@st.cache_data
def get_data():
    meta = pd.read_csv('movie_recommendation_file.csv')
    return meta

meta = get_data()

@st.cache_data
def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['overview'] = dataframe['overview'].fillna('')
    dataframe['overview'] = dataframe['overview'] + ' ' + dataframe['title'] + ' ' + dataframe['genres']
    tfidf_matrix = tfidf.fit_transform(dataframe['overview'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = calculate_cosine_sim(meta)


@st.cache_data
def get_popular_movies():
    popular_movies = pd.read_csv('popular_movies.csv')
    return popular_movies

popular_movies = get_popular_movies()

@st.cache_data
def get_action_popular():
    action_popular = pd.read_csv('action_popular.csv')
    return action_popular

action_popular = get_action_popular()

@st.cache_data
def get_science_fiction_popular():
    science_fiction_popular = pd.read_csv('science_fiction_popular.csv')
    return science_fiction_popular

science_fiction_popular = get_science_fiction_popular()

@st.cache_data
def get_drama_popular():
    drama_popular = pd.read_csv('drama_popular.csv')
    return drama_popular

drama_popular = get_drama_popular()

@st.cache_data
def get_thriller_popular():
    thriller_popular = pd.read_csv('thriller_popular.csv')
    return thriller_popular

thriller_popular = get_thriller_popular()

@st.cache_data
def get_comedy_popular():
    comedy_popular = pd.read_csv('comedy_popular.csv')
    return comedy_popular

comedy_popular = get_comedy_popular()

def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    movie_index = indices[title]
    # Benzerlik skorlarını alma
    similarity_scores = cosine_sim[movie_index]
    # Eğer similarity_scores 3D bir dizi ise (örneğin, [1, 9548, 9548]), 2D'ye dönüştürme
    if similarity_scores.ndim == 3:
        similarity_scores = similarity_scores.squeeze()  # 3D'den 2D'ye sıkıştırma
    # Benzerlik skorlarını DataFrame'e dönüştürme
    similarity_scores_df = pd.DataFrame(similarity_scores, index=dataframe.index, columns=["score"])
    # Kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores_df.sort_values(by="score", ascending=False).index[1:11]
    # Film bilgilerini döndürme
    return dataframe.loc[movie_indices]


col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown('<div style="width:277px;height:277px;"><img src="https://media1.tenor.com/m/O-yqDCMQTFoAAAAd/god-i-love-it-red.gif" style="width:100%; height:100%; object-fit:cover;"></div>', 
                unsafe_allow_html=True)

with col2:
    st.markdown('<div style="width:277px;height:277px;"><img src="https://media1.tenor.com/m/l4PRWJ68WWYAAAAd/i-understand-don-vito-corleone.gif" style="width:100%; height:100%; object-fit:cover;"></div>', 
                unsafe_allow_html=True)

with col3:
    st.markdown('<div style="width:277px;height:277px;"><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWFxaTEzd2phcW13a3JveGd6aTZtN2UxZjM5azBiYzc3dDUwdTA0YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u7uiWWbRFC2TC/giphy.gif" style="width:100%; height:100%; object-fit:cover;"></div>', 
                unsafe_allow_html=True)

with col4:
    st.markdown('<div style="width:277px;height:277px;"><img src="https://media1.tenor.com/m/B_p2kigHBqMAAAAd/deadpool-dance-bye-bye-bye.gif" style="width:100%; height:100%; object-fit:cover;"></div>', 
                unsafe_allow_html=True)

with col5:
    st.markdown('<div style="width:277px;height:277px;"><img src="https://media1.tenor.com/m/V24w9mQa-nQAAAAd/%D8%A7%D9%84%D9%85%D9%88%D8%B3%D9%8A%D9%82%D8%A7%D8%B1.gif" style="width:100%; height:100%; object-fit:cover;"></div>', 
                unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

home_tab, recommendation_tab = st.tabs(['Home', 'Recommend'])

movie_genres = {
    'Popular Movies': popular_movies,
    'Action Popular': action_popular,
    'Science Fiction Popular': science_fiction_popular,
    'Drama Popular': drama_popular,
    'Comedy Popular': comedy_popular,
    'Thriller Popular': thriller_popular
}

with home_tab:
    st.header("Welcome to :rainbow[Miuultainment]")
    
    for genre_header, movie_df in movie_genres.items():
        st.subheader(genre_header)
        cols = st.columns(10)  # Create 10 columns
        
        for index, row in movie_df.iterrows():
            col = cols[index % 10]  # Place each movie in one of the columns
            movie_title = row['title']
            imdb_id = row['imdb_id']
            
            # Get movie poster URL from IMDb
            image_url = get_image_from_imdb(imdb_id)
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/"
            
            if image_url:
                # Create clickable image
                col.markdown(
                    f'<a href="{imdb_url}" target="_blank">'
                    f'<img src="{image_url}" width="200" style="display: block; margin-left: auto; margin-right: auto;">'
                    f'</a>',
                    unsafe_allow_html=True
                )
            else:
                col.write("No image available")
            
            # Display movie title
            col.markdown(f'<p style="font-size: 14px; text-align: center;">{movie_title}</p>', unsafe_allow_html=True)

with recommendation_tab:
    st.header('Welcome to the :rainbow[Movie Recommender]')
    movie_col1, movie_col2, movie_col3 = st.columns([1, 2, 1])
    selected_movie = movie_col2.selectbox('Choose a movie you like.', options=meta.title.unique())

    recommendations_df = content_based_recommender(title=selected_movie, cosine_sim=cosine_sim, dataframe=meta)
    
    # İlk 5 filmi göstermek için 5 kolon
    row1_cols = st.columns(5)
    # Sonraki 5 filmi göstermek için 5 kolon
    row2_cols = st.columns(5)

    tmdbcol1, tmdbcol2, tmdbcol3 = st.columns([1, 0.5, 1], gap='large')
    recommend_button = tmdbcol2.button('Recommend a Movie')

    if recommend_button:
        for index, movie_col in enumerate(row1_cols + row2_cols):
            if index < len(recommendations_df):
                movie_row = recommendations_df.iloc[index]
                movie_id = movie_row['id']
                movie_title = movie_row['title']

                # `meta` DataFrame'inde film ID'sine göre arama yap
                movie = meta.loc[meta['id'] == movie_id]  # Meta DataFrame'inde id sütununa göre arama yap

                if movie.empty:
                    continue  # Film bulunamadıysa bir sonraki filme geç

                imdb_id = movie['imdb_id'].values[0]
                image_url = get_image_from_imdb(imdb_id)
                imdb_url = f"https://www.imdb.com/title/{imdb_id}/"

                if image_url:
                    movie_col.markdown(
                        f'<a href="{imdb_url}" target="_blank">'
                        f'<img src="{image_url}" width="200" style="display: block; margin-left: auto; margin-right: auto;">'
                        f'</a>',
                        unsafe_allow_html=True
                    )
                else:
                    movie_col.write("No image available")
                
                movie_col.markdown(f'<p style="font-size: 14px; text-align: center;">{movie_title}</p>', unsafe_allow_html=True)
