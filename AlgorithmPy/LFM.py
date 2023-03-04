import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split

from DatabaseAPI import RatingAPI


def run_LFM():
    data_from_sql = RatingAPI.select_all()
    data_list = list()
    # df = pd.DataFrame(columns=['userId', 'movieId', 'rating']
    for x in data_from_sql:
        data_list.append({'userId': x.userId, 'movieId': x.movieId, 'rating': x.rating})
    df = pd.DataFrame(data_list)
    reader = Reader(rating_scale=(1, 5), line_format='user item rating timestamp')
    data = Dataset.load_from_df(df, reader)
    train_set, test_set = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(train_set)
    

if __name__ == '__main__':
    run_LFM()
