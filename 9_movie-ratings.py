
movie_ratings = {
    "The Prestige": 9,
    "Bee Movie": 7,
    "Mission Impossible: Fallout": 4,
    "Avengers Endgame": 7,
    "Star Wars Attack of the Clones": 2
}


def recommend_movie(movie_ratings, movie_title):
    if movie_title in movie_ratings:
        if movie_ratings[movie_title] >= 8:
            print(f"I recommend watching '{movie_title}'. It has a rating of {movie_ratings[movie_title]}/10.")
        else:
            print(f"I'm sorry, '{movie_title}' doesn't have a high rating. Here are some other recommendations:")
    else:
        print("Movie not found. Here are some recommendations:")
    
    recommended_movies = [movie for movie, rating in movie_ratings.items() if rating >= 8]
    for movie in recommended_movies:
        print(f"- {movie}")


user_movie = input("Enter a movie title: ")


recommend_movie(movie_ratings, user_movie)