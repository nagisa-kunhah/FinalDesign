from sqlalchemy import Column, Integer, FLOAT, PrimaryKeyConstraint
from sqlalchemy import create_engine, select, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped
import pymysql

Base = declarative_base()
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class RatingRecord(Base):
    __tablename__ = 'rating'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[float]
    timestamp: Mapped[int]

    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def __repr__(self):
        return "<RatingRecord(userId='%s', movieId='%s', rating='%s' timestamp='%s')>" % (
            self.user_id, self.movie_id, self.rating, self.timestamp)


Base.metadata.create_all(engine)


def add(records):
    session = session_factor()
    for item in records:
        session.add(item)
    session.commit()


def select_all():
    session = session_factor()
    res = session.query(RatingRecord).all()
    return res


def select_recent_k(user_id, k):
    session = session_factor()
    stmt = select(RatingRecord).where(RatingRecord.user_id == user_id).order_by(desc(RatingRecord.timestamp)).limit(
        limit=k)
    res = session.scalars(stmt)
    session.commit()
    return list(res)


if __name__ == '__main__':
    '''
    # m = RatingRecord(1, 1, 4.0, 964982703)
    # x = list()
    # x.append(m)
    # add(x)
    '''
    tmp = select_all()
    print(tmp)
