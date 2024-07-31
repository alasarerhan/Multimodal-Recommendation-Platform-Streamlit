
import streamlit as st
import pandas as pd
from scrape import get_image_from_imdb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import folium
from streamlit_folium import folium_static, st_folium
from sklearn.neighbors import NearestNeighbors
import folium
from folium.plugins import MarkerCluster
from sklearn.preprocessing import StandardScaler
import streamlit.components.v1 as components

st.set_page_config(layout= 'wide', page_title = 'Miuultainment')


@st.cache_data
def get_data():
    meta = pd.read_csv('data/movie_recommendation_file.csv')
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



st.image('C:/Users/erhan/OneDrive/Resimler/miuulentertainment.gif',width=1400)
st.title(':rainbow[MIUULtainment] :house: :movie_camera: :video_game:  :green_book: 🎶')

st.markdown('**Miuultainment: Enjoy a Unique Experience of Entertainment!**')
st.write("""Welcome to Miuultainment, the innovative recommendation site that caters to all your entertainment needs in one place.
Whether you're searching for a fantastic Airbnb for your next vacation, an enchanting book to read, a captivating movie to watch,
 an exciting game to play, or some new music to enjoy, Miuultainment has got you covered.""")



home_tab, airbnb_tab, amazon_tab, tmdb_tab, metacritic_tab = st.tabs(["Home","AirBnb", "Amazon", "TMDB", "MetaCritic"])


 
with st.container():  # 'home_tab' yerine st.container kullanın
    st.header('Discover Your Next Adventure')
    st.write("""At Miuultainment, we believe that every experience should be extraordinary. 
    Our platform curates personalized recommendations based on your preferences, ensuring that you find the perfect match every time.""")

    col_airbnb, col_amazon, col_movie, col_game = st.columns(4)
    

    #! airbnb column
    col_airbnb.header('Stay in the Best Places')
    image_airbnb = 'https://media1.tenor.com/m/rsSIoLjds9UAAAAC/airbnb-door.gif'
    redirect_airbnb = "https://www.airbnb.com.tr/"
    html_airbnb = f"""<a href="{redirect_airbnb}" target="_blank"><img src="{image_airbnb}" style="width:300px;height:200px;"></a>"""
    col_airbnb.markdown(html_airbnb, unsafe_allow_html=True)
    
    col_airbnb.write("""Explore our extensive collection of top-rated Airbnb's. 
                    From cozy cabins in the woods to luxurious city apartments, we provide you with the best options to make your stay unforgettable.""")


    #! imdb column
    col_movie.header('Watch Captivating Movies')
    image_movie = 'https://media.tenor.com/S1r_YTIOtKgAAAAM/movie-bored.gif'
    redirect_movie = "https://appent-g9qe2nhwhrvvgnhkqybvzq.streamlit.app/"
    html_movie = f"""<a href="{redirect_movie}" target="_blank"><img src="{image_movie}" style="width:300px;height:200px;"></a>"""
    col_movie.markdown(html_movie, unsafe_allow_html=True)

    col_movie.write("""Enjoy a cinematic experience with our movie suggestions. Whether you’re into thrillers, comedies, dramas, or documentaries,
                Miuultainment ensures you never run out of great movies to watch.""")

    
    #! amazon column
    col_amazon.header('Read Engaging Books')
    image_amazon = "https://media1.tenor.com/m/e45JF2Wtvv0AAAAC/cat99-cat999.gif"
    redirect_amazon = "https://www.amazon.com/Best-Books-of-2024-So-Far/b?ie=UTF8&node=3003015011"
    html_amazon = f"""<a href="{redirect_amazon}" target="_blank"><img src="{image_amazon}" style="width:300px;height:200px;"></a>"""
    col_amazon.markdown(html_amazon, unsafe_allow_html=True)
    col_amazon.write("""Dive into our selection of engaging books.
                From thrilling mysteries to heartwarming romances, find the perfect read to captivate your mind and spirit.""")


    #! steam column
    col_game.header('Play Exciting Games')
    image_steam = "https://media1.tenor.com/m/zjbXreUb5_YAAAAd/steam.gif"
    redirect_steam = "https://store.steampowered.com/"
    html_steam = html_movie = f"""<a href="{redirect_steam}" target="_blank"><img src="{image_steam}" style="width:300px;height:200px;"></a>"""
    col_game.markdown(html_steam, unsafe_allow_html=True)

    col_game.write("""Level up your gaming experience with our curated game recommendations. 
                From action-packed adventures to mind-bending puzzles, find the perfect game to keep you entertained for hours.""")
    
    
 
#! TMDB tab
with tmdb_tab:
    tmdb_col1, tmdb_col2, tmdb_col3 = tmdb_tab.columns([1,2,1])
    selected_movie = tmdb_col2.selectbox('Choose a movie you like.', options= meta.title.unique())

    recommendations_df = content_based_recommender(title=selected_movie,cosine_sim=cosine_sim,dataframe=meta)
    movie_1, movie_2, movie_3, movie_4, movie_5 = tmdb_tab.columns(5)
    movie_6, movie_7, movie_8, movie_9, movie_10 = tmdb_tab.columns(5)


    tmdbcol1, tmdbcol2, tmdbcol3 = tmdb_tab.columns([1,0.5,1], gap='large')
    recommend_button = tmdbcol2.button('Recommend a Movie')

    if recommend_button:
        # Önerilen filmleri göster
        for index, movie_col in enumerate([movie_1, movie_2, movie_3, movie_4, movie_5,movie_6, movie_7, movie_8, movie_9, movie_10]):
            # `recommendations_df` DataFrame'inden film ID'sini ve başlığını al
            if index < len(recommendations_df):
                movie_row = recommendations_df.iloc[index]
                movie_id = movie_row['id']
                movie_title = movie_row['title']
                
                # `meta` DataFrame'inde film ID'sine göre arama yap
                movie = meta.loc[meta['id'] == movie_id]  # Meta DataFrame'inde id sütununa göre arama yap

                if movie.empty:
                    continue  # Film bulunamadıysa bir sonraki filme geç
                
                imdb_id = movie['imdb_id'].values[0]  # Numpy array'den str'e dönüştürme

                movie_col.subheader(f"**{movie_title}**")

                # Resim URL'sini alma ve kontrol etme
                image_url = get_image_from_imdb(imdb_id)
                if image_url:
                    movie_col.image(image_url,width = 200, use_column_width=True)

