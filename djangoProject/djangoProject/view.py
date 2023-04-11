from djangoProject import LFM
from django.http import HttpResponse
from djangoProject import OnlineRecommend


def fresh_recommend(request):
    LFM.enter()
    return HttpResponse("ok")


def online_update(request):
    user_id = request.GET.get('user_id')
    movie_id = request.GET.get('movie_id')
    OnlineRecommend.OnlineUpdate(int(user_id), int(movie_id))
    return HttpResponse('ok')
