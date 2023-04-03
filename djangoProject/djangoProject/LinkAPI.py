from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pandas as pd
import pymysql

Base = declarative_base()
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class Link(Base):
    __tablename__ = 'Link'

    movieId = Column(Integer, primary_key=True, autoincrement=True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)

    def __init__(self, move_id, imdb_id, tmdb_id):
        self.movieId = move_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id

    def __repr__(self):
        return "<Link(movieId='%s', imdbId='%s', tmdbId='%s')>" % (
            self.movieId, self.imdbId, self.tmdbId)


Base.metadata.create_all(engine)


def add(links: list):
    session = session_factor()
    for x in links:
        session.add(x)
    session.commit()
