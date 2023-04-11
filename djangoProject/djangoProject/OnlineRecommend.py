import os.path

import surprise
from surprise import KNNBasic
from surprise import Trainset
import numpy as np
from djangoProject import MovieInOutAPI
from djangoProject import RatingAPI
from djangoProject import recommendAPI


def OnlineUpdate(user_id, movie_id):
    """
    :param user_id:
    :param movie_id:
    :return: None
    """
    model_file = os.path.expanduser('./dump_files/knn_model')
    train_set_file = os.path.expanduser('./dump_files/train_set')
    model: KNNBasic = surprise.dump.load(model_file)[0]
    train_set: Trainset = surprise.dump.load(train_set_file)[0]
    print(model is not None)
    print(train_set is not None)
    # neighbors: np.ndarray = model.get_neighbors(train_set.to_inner_iid(movie_id), 20)
    # print(neighbors)
    recommend = recommendAPI.select_by_uid(user_id)
    recommend_iid = [x.movie_id for x in recommend]
    in_out = MovieInOutAPI.SelectByMovieIds(recommend_iid)
    recent_k_record = RatingAPI.select_recent_k(user_id, 20)
    in_num = list()
    out_num = list()
    for x in in_out:
        x: MovieInOutAPI.MovieInOutAPI
        in_num.append(max(x.in_cnt, 1))
        out_num.append(max(x.out_cnt, 1))
    in_num = np.array(in_num)
    out_num = np.array(out_num)
    increase_factor = np.log(in_num)
    decrease_factor = np.log(out_num)
    n = len(recommend_iid)
    recommend_inner_id = [train_set.to_inner_iid(x) for x in recommend_iid]
    sum_sim = np.sum(model.sim[movie_id][recommend_inner_id])
    for i in range(n):
        x = recommend[i]
        x: recommendAPI.RecommendRecord
        now_factor = model.sim[train_set.to_inner_iid(movie_id)][train_set.to_inner_iid(x.movie_id)] / sum_sim
        now_factor += increase_factor[i]
        now_factor -= decrease_factor[i]
        x.online_rating = x.online_rating * 0.3 + now_factor * 0.7
        recommend[i] = x
    recommendAPI.Update(records=recommend)
