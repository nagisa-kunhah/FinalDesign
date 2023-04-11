from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column

Base = declarative_base()
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username="root", pwd="root", host="127.0.0.1", port="3306", db="test")
engine = create_engine(DB_URI)
session_factor = sessionmaker(bind=engine)


class MovieInOutAPI(Base):
    __tablename__ = 'movie_in_out'
    movie_id: Mapped[int] = mapped_column(primary_key=True)
    in_cnt: Mapped[int]
    out_cnt: Mapped[int]

    def __init__(self, movie_id, in_cnt, out_cnt):
        self.movie_id = movie_id
        self.in_cnt = in_cnt
        self.out_cnt = out_cnt

    def __repr__(self):
        return "<movie_in_out:{} {} {}>".format(self.movie_id, self.in_cnt, self.out_cnt)


def Insert(records):
    session = session_factor()
    for item in records:
        session.add(item)
    session.commit()


def SelectByMovieIds(ids):
    stmt = select(MovieInOutAPI).where(MovieInOutAPI.movie_id.in_(ids))
    session = session_factor()
    res = session.scalars(stmt).all()
    session.commit()
    re = dict()
    for i in range(len(ids)):
        re[ids[i]] = i
    res = list(res)
    res.sort(key=lambda x: re[x.movie_id])
    # print()
    # print(res)
    # print(type(res))
    # print(res)

    # for i in range(len(ids)):
    #     re[ids[i]] = i
    return res
