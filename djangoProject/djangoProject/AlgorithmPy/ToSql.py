import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from DatabaseAPI import LinkAPI
from DatabaseAPI import RatingAPI
from DatabaseAPI.LinkAPI import Link
from djangoProject.djangoProject.AlgorithmPy.DatabaseAPI import MoviesAPI

# from DatabaseAPI.MoviesAPI import Movie, add

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test',
                       encoding='utf-8',
                       echo=True)


def init_link():
    df = pd.read_csv('data/links.csv')
    n = len(df)
    a = []
    for i in range(n):
        row = df.iloc[[i]]
        movie_id = str(row['movieId'].item())
        imdb_id = str(row['imdbId'].item())
        tmdb_id = str(row['tmdbId'].item())
        if tmdb_id == 'nan':
            tmdb_id = '-1'
        # mx1 = max(mx1, len(movie_id))
        # mx2 = max(mx2, len(title))
        # mx3 = max(mx3, len(genres))
        # print("{}:{} {} {}".format(i, movie_id, imdb_id, tmdb_id))
        a.append(Link(movie_id, imdb_id, tmdb_id))
    LinkAPI.add(a)


def init_movies():
    df = pd.read_csv('data/movies.csv')
    n = len(df)
    a = []
    # print(df)
    # mx1 = 0
    # mx2 = 0
    # mx3 = 0
    for i in range(n):
        row = df.iloc[[i]]
        movie_id = str(row['movieId'].item())
        title = str(row['title'].item())
        genres = str(row['genres'].item())
        print(genres)
        if genres == "NULL":
            genres = '-1'
        # mx1 = max(mx1, len(movie_id))
        # mx2 = max(mx2, len(title))
        # mx3 = max(mx3, len(genres))
        # print("{}{}{}".format(movie_id, title, genres))
        a.append(MoviesAPI.Movie(movie_id, title, genres))
    MoviesAPI.add(a)


def init_rating():
    df = pd.read_csv('data/ratings.csv')
    n = len(df)
    a = []
    # mx1 = 0
    # mx2 = 0
    # mx3 = 0
    for i in range(n):
        row = df.iloc[[i]]
        user_id = str(row['userId'].item())
        movie_id = str(row['movieId'].item())
        rating = float(row['rating'].item())
        # mx1 = max(len(user_id), mx1)
        # mx2 = max(len(movie_id), mx2)
        # mx3 = max(len(rating), mx3)
        a.append(RatingAPI.RatingRecord(user_id, movie_id, rating, 0))
    RatingAPI.add(a)


# init_rating()
init_link()
init_movies()
init_rating()
