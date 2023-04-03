from collections import defaultdict

import pandas as pd
from surprise import Reader, Dataset, dataset, SVD

from djangoProject import RatingAPI
from djangoProject import recommendAPI

model = None


def get_top_n(predictions, n):
    """Return the top-N recommendation for each user from a set of predictions.

        Args:
            predictions(list of Prediction objects): The list of predictions, as
                returned by the test method of an algorithm.
            n(int): The number of recommendation to output for each user. Default
                is 10.

        Returns:
        A dict where keys are user (raw) ids and values are lists of tuples:
            [(raw item id, rating estimation), ...] of size n.
        """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def run_LFM():
    print("run LFM")
    data_from_sql = RatingAPI.select_all()
    data_list = list()
    user_set = set()
    movie_set = set()
    for x in data_from_sql:
        data_list.append({'userId': x.userId, 'movieId': x.movieId, 'rating': x.rating})
        user_set.add(x.userId)
        movie_set.add(x.movieId)
    df = pd.DataFrame(data_list)
    reader = Reader(rating_scale=(1, 5), line_format='user item rating timestamp')
    data = Dataset.load_from_df(df, reader)
    train_set = dataset.DatasetAutoFolds.build_full_trainset(data)
    global model
    model = SVD()
    model.fit(train_set)
    test_set = train_set.build_anti_testset()
    prediction = model.test(test_set)
    top_n = get_top_n(prediction, n=10)
    recommend_records = list()
    # print(top_n)
    for user_id in top_n:
        for movie_id, _ in top_n[user_id]:
            recommend_records.append(recommendAPI.RecommendRecord(user_id=user_id, movie_id=str(movie_id)))
    # print(recommend_records[0])
    recommendAPI.add(records=recommend_records)


if __name__ == '__main__':
    run_LFM()
