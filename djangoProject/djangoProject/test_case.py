from django.test import TestCase
from djangoProject import LFM
from djangoProject import recommendAPI
from surprise import dump
from djangoProject import OnlineRecommend
from djangoProject import RatingAPI
from djangoProject import MovieInOutAPI
from djangoProject import OnlineRecommend


class RecommendAPI(TestCase):
    def test_case1(self):
        LFM.enter()

    def test_case3(self):
        da = RatingAPI.select_all()
        res = dict()
        for x in da:
            x: RatingAPI.RatingRecord
            if x.movie_id not in res:
                res[x.movie_id] = [0, 0]
            if x.rating >= 2.5:
                res[x.movie_id][0] += 1
            else:
                res[x.movie_id][1] += 1
        # print(res)
        records = []
        for item in res.keys():
            obj = MovieInOutAPI.MovieInOutAPI(movie_id=item, in_cnt=res[item][0], out_cnt=res[item][1])
            records.append(obj)
            # print(obj)
            # break
        MovieInOutAPI.Insert(records)

    def test_case3(self):
        MovieInOutAPI.SelectByMovieIds([2, 1, 3])

    def test_case4(self):
        OnlineRecommend.OnlineUpdate(1, 2)

    def test_case5(self):
        print(RatingAPI.select_recent_k(1, 3))

    def test_case6(self):
        recommendAPI.select_by_uid(1)

    def test_case7(self):
        recommendAPI.Update([recommendAPI.RecommendRecord(1, 2, 4, 0)])

    def test_case8(self):
        a = recommendAPI.RecommendRecord(1, 2, 3, 3.5)
        b = recommendAPI.RecommendRecord(1, 2, 4, 3.5)
        recommendAPI.Update([a, b])
