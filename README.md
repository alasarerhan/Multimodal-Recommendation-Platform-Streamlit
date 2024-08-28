# Miuul Entertainment - Recommendation System
## Business Problem
A comprehensive recommendation system has been developed to provide personalized suggestions for Airbnb homes, anime, games, movies, and books. The goal is to enhance user experience by predicting user preferences and recommending relevant content across these categories. The movie recommendation component uses content-based filtering to suggest films similar to the ones users have selected.

## About Datasets
### Airbnb Dataset
Airbnb is an online marketplace for vacation home rentals and tourism activities. This dataset describes the listing activities of bed and breakfasts in New York City. The dataset contains various attributes such as neighborhood, room type, price, and availability, which are used to recommend suitable Airbnb homes to users.

### Anime Dataset
The anime dataset from MyAnimeList.net contains information about various anime series, including genres, studios, ratings, and user reviews. The system predicts the ratings users would give to anime they haven’t watched and suggests similar anime based on their preferences.

### Game Dataset
The game dataset contains information about games available on Steam, such as release dates, platform availability, ratings, and user reviews. The system recommends games based on their attributes and the similarity to games users have shown interest in.

### Movie Dataset
This dataset is used to provide personalized movie recommendations based on movie metadata such as genres, overview, and user ratings. Movie posters and details are fetched from IMDb to enrich the user experience.

### Book Dataset
This dataset includes user ratings and metadata from Amazon for over 200,000 unique books. The recommendation system suggests books based on user preferences and the attributes of books they have rated.

### Solution
The recommendation system leverages a combination of machine learning techniques and content-based filtering to analyze user preferences and provide tailored recommendations across different content types:

Airbnb: The system uses unsupervised learning methods, specifically K-Means clustering, to categorize listings based on features like location, price, and room type. Folium is then used to visualize these clusters on an interactive map, helping users find the most suitable Airbnb homes.

Movies, Games, and Books: Item-based and user-based filtering techniques are applied to recommend content similar to what users have shown interest in or rated highly.

Anime: In addition to item-based and user-based filtering, the system employs model-based filtering using XGBoost. This approach predicts the ratings users would give to anime they haven’t watched yet, providing more accurate and personalized recommendations.

Each recommendation engine within the system is designed to handle the specific attributes and nuances of the content it suggests, ensuring that users receive the most relevant and engaging suggestions across all categories.

### How It Works
Personalized Recommendations: Users can interact with the system to receive recommendations for Airbnb homes, anime, games, movies, and books.
Rich Visuals: The system integrates with external APIs to fetch images and additional content details, enhancing the user experience.
# Visit our site: https://miuulentertainment.streamlit.app/
