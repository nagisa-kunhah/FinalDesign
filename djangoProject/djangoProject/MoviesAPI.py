from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pymysql
import pandas as pd
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
Base = declarative_base()
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class Movie(Base):
    __tablename__ = 'Movies'

    movieId = Column(String(16), primary_key=True)
    title = Column(String(256))
    genres = Column(String(128))

    def __init__(self, movie_id, title, genres):
        self.movieId = movie_id
        self.title = title
        self.genres = genres

    def __repr__(self):
        return "<Movie(movieId='%s', title='%s', genres='%s')>" % (
            self.movieId, self.title, self.genres)


Base.metadata.create_all(engine)


def add(movies: list):
    session = session_factor()
    for movie in movies:
        session.add(movie)
    session.commit()


if __name__ == '__main__':
    m = Movie('1', 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy')
    x = list()
    x.append(m)
    add(x)
