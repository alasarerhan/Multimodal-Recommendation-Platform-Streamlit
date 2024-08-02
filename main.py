import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(layout= 'wide', page_title = 'Miuultainment')

st.image('miuulentertainment.gif',width=1400)
st.title(':rainbow[MIUULtainment] :house: :movie_camera: :video_game:  :green_book: 🎶')


with st.container():  # 'home_tab' yerine st.container kullanın
    st.header('Discover Your Next Adventure with :blue[AI] Powered Recommendations')
    st.write("""At Miuultainment, we believe that every experience should be extraordinary. 
    Our platform curates personalized recommendations based on your preferences, ensuring that you find the perfect match every time.""")

    col_airbnb, col_amazon, col_movie, col_game, col_anime = st.columns(5)


    #! airbnb column
    col_airbnb.header('Stay in the Best Places')
    image_airbnb = 'https://media1.tenor.com/m/rsSIoLjds9UAAAAC/airbnb-door.gif'
    redirect_airbnb = "https://www.airbnb.com.tr/"
    html_airbnb = f"""<a href="{redirect_airbnb}" target="_blank"><img src="{image_airbnb}" style="width:250px; height:200px;"></a>"""
    col_airbnb.markdown(html_airbnb, unsafe_allow_html=True)

    col_airbnb.write("""
        <div style="text-align: justify;">
        Explore our extensive collection of top-rated Airbnb's. From cozy cabins in the woods to luxurious city apartments, 
        we provide you with the best options to make your stay unforgettable.
        </div>""", unsafe_allow_html=True)


    #! imdb column
    col_movie.header('Watch Great Movies')
    image_movie = 'https://media.tenor.com/HJTXKCtOYwgAAAAM/perfect-popcorn.gif'
    redirect_movie = "https://appent-g9qe2nhwhrvvgnhkqybvzq.streamlit.app/"
    html_movie = f"""<a href="{redirect_movie}" target="_blank"><img src="{image_movie}" style="width:250px; height:200px;"></a>"""
    col_movie.markdown(html_movie, unsafe_allow_html=True)

    col_movie.write("""
        <div style="text-align: justify;">
        Enjoy a cinematic experience with our movie suggestions. Whether you’re into thrillers, comedies, dramas, or documentaries,
        Miuultainment ensures you never run out of great movies to watch.
        </div>""", unsafe_allow_html=True)



    #! amazon column
    col_amazon.header('Read Engaging Books')
    image_amazon = "https://media1.tenor.com/m/e45JF2Wtvv0AAAAC/cat99-cat999.gif"
    redirect_amazon = "https://www.amazon.com/Best-Books-of-2024-So-Far/b?ie=UTF8&node=3003015011"
    html_amazon = f"""<a href="{redirect_amazon}" target="_blank"><img src="{image_amazon}" style="width:250px; height:200px;"></a>"""
    col_amazon.markdown(html_amazon, unsafe_allow_html=True)
    col_amazon.write("""
                <div style="text-align: justify;">
                Dive into our selection of engaging books.
                From thrilling mysteries to heartwarming romances, find the perfect read to captivate your mind and spirit.
                </div>""", unsafe_allow_html=True)


    #! steam column
    col_game.header('Play Exciting Games')
    image_steam = "https://media1.tenor.com/m/zjbXreUb5_YAAAAd/steam.gif"
    redirect_steam = "https://store.steampowered.com/"
    html_steam = f"""<a href="{redirect_steam}" target="_blank"><img src="{image_steam}" style="width:250px; height:200px;"></a>"""
    col_game.markdown(html_steam, unsafe_allow_html=True)

    col_game.write("""
                <div style="text-align: justify;">
                Level up your gaming experience with our curated game recommendations. 
                From action-packed adventures to mind-bending puzzles, find the perfect game to keep you entertained for hours.
                </div>""", unsafe_allow_html=True)

    
    #! Anime column
    col_anime.header('Watch Fantastic Animes')
    image_anime = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTE4bWtqbHFqd3lma2Vla3duMTB2dWNlOHNndnl3aHh5bmF0cmZsZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11KzOet1ElBDz2/giphy.webp"
    redirect_anime = "https://deathnote.fandom.com/wiki/Death_Note_Wiki"
    html_anime = f"""<a href="{redirect_anime}" target="_blank"><img src="{image_anime}" style="width:250px; height:200px;"></a>"""
    col_anime.markdown(html_anime, unsafe_allow_html=True)

    col_anime.write("""
                    <div style="text-align: justify;">
                    Explore our anime selection! From epic adventures to touching stories, 
                    discover the perfect series to engage and entertain you.
                    </div>""", unsafe_allow_html=True)