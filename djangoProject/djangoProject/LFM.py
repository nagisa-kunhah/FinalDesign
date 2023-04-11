from collections import defaultdict
import os
import pandas as pd
import surprise
from surprise import Reader, Dataset, dataset, SVD, KNNBasic

from djangoProject import RatingAPI
from djangoProject import recommendAPI
from djangoProject import SimilarMovieAPI


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


def enter():
    print("run")
    data_from_sql = RatingAPI.select_all()
    data_list = list()
    user_set = set()
    movie_set = set()
    for x in data_from_sql:
        data_list.append({'userId': x.user_id, 'movieId': x.movie_id, 'rating': x.rating})
        user_set.add(x.user_id)
        movie_set.add(x.movie_id)
    print('movie_num:', len(movie_set))
    df = pd.DataFrame(data_list)
    reader = Reader(rating_scale=(1, 5), line_format='user item rating timestamp')
    data = Dataset.load_from_df(df, reader)
    train_set = dataset.DatasetAutoFolds.build_full_trainset(data)
    run_LFM(train_set)
    run_KNN(train_set, movie_set)


def run_LFM(train_set):
    model = SVD()
    model.fit(train_set)
    test_set = train_set.build_anti_testset()
    prediction = model.test(test_set)
    top_n = get_top_n(prediction, n=10)
    recommend_records = list()
    for user_id in top_n:
        for movie_id, rating in top_n[user_id]:
            recommend_records.append(
                recommendAPI.RecommendRecord(user_id=user_id, movie_id=str(movie_id), rating=rating))
    recommendAPI.add(records=recommend_records)
    print("finished LFM")


def run_KNN(train_set, movie_set):
    print("run_KNN")

    model = KNNBasic(sim_options={
        "name": "cosine",
        "user_based": False,
    })
    model_name = os.path.expanduser('./dump_files/knn_model')
    train_set_file = os.path.expanduser('./dump_files/train_set')
    model.fit(train_set)
    surprise.dump.dump(model_name, model)
    surprise.dump.dump(train_set_file, train_set)
    print('dump finished')


if __name__ == '__main__':
    enter()
