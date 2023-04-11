import json

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped

Base = declarative_base()
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class SimilarMovieRecord(Base):
    __tablename__ = 'similar_movie'

    movie_id: Mapped[int] = mapped_column(primary_key=True)
    similar_movie: Mapped[int] = mapped_column(primary_key=True)

    def __init__(self, movie_id, similar_movie):
        self.movie_id = movie_id
        self.similar_movie = similar_movie

    def __repr__(self):
        return "<similar_movie({},{})>".format(self.movie_id, self.similar_movie)


def add(records):
    session = session_factor()
    session.query(SimilarMovieRecord).delete()
    print(records[:20])
    for item in records:
        session.add(item)
    session.commit()
    # session.commit()


def select_all():
    session = session_factor()
    res = session.query(SimilarMovieRecord).all()
    return res


def select_by_movie_id(movie_id):
    pass
