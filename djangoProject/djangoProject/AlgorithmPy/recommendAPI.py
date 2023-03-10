from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:root@localhost:3306/test',
                       encoding='utf-8',
                       echo=True)
session_factor = sessionmaker(bind=engine)


class RecommendRecord(Base):
    __tablename__ = 'recommend'

    user_id = Column(Integer)
    movie_id = Column(String(255))
    PrimaryKeyConstraint(user_id, movie_id)

    def __init__(self, user_id, movie_id):
        self.user_id = user_id
        self.movie_id = movie_id

    def __repr__(self):
        return "<RecommendRecord({},{})>".format(self.user_id, self.movie_id)


def add(records):
    session = session_factor()
    for item in records:
        print(item)
    for item in records:
        session.add(item)
    session.commit()


def select_all():
    session = session_factor()
    res = session.query(RecommendRecord).all()
    return res


if __name__ == '__main__':
    print("work!!")
