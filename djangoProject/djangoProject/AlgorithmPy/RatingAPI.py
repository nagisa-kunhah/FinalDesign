from sqlalchemy import Column, Integer, FLOAT, PrimaryKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test',
                       encoding='utf-8',
                       echo=True)
session_factor = sessionmaker(bind=engine)


class RatingRecord(Base):
    __tablename__ = 'Rating'

    userId = Column(Integer)
    movieId = Column(Integer)
    rating = Column(FLOAT)
    timestamp = Column(Integer)
    PrimaryKeyConstraint(userId, movieId)

    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def __repr__(self):
        return "<RatingRecord(userId='%s', movieId='%s', rating='%s' timestamp='%s')>" % (
            self.userId, self.movieId, self.rating, self.timestamp)


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


if __name__ == '__main__':
    '''
    # m = RatingRecord(1, 1, 4.0, 964982703)
    # x = list()
    # x.append(m)
    # add(x)
    '''
    tmp = select_all()
    print(tmp)
