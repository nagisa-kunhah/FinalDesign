import json

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy import create_engine, select, update, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped

Base = declarative_base()
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class RecommendRecord(Base):
    __tablename__ = 'recommend'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[float]
    online_rating: Mapped[float]

    def __init__(self, user_id, movie_id, rating, online_rating=0.0):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.online_rating = online_rating

    def __repr__(self):
        return "<RecommendRecord({},{}),{},{}>".format(self.user_id, self.movie_id, self.rating, self.online_rating)


def add(records):
    session = session_factor()
    session.query(RecommendRecord).delete()
    for item in records:
        session.add(item)
    session.commit()
    # session.commit()


def select_all():
    session = session_factor()
    res = session.query(RecommendRecord).all()
    return res


def select_by_uid(user_id) -> list:
    stmt = select(RecommendRecord).where(RecommendRecord.user_id == user_id)
    session = session_factor()
    ret = session.scalars(stmt)
    session.commit()
    ret = list(ret)
    return ret


def Update(records: list) -> list:
    """
    :param records:
    :return:
    """
    session = session_factor()
    for x in records:
        stmt = update(RecommendRecord) \
            .where(
            and_(RecommendRecord.user_id == x.user_id, RecommendRecord.movie_id == x.movie_id)
        ) \
            .values(rating=x.rating, online_rating=x.online_rating)
        # print(stmt)
        session.execute(stmt)
    session.commit()
