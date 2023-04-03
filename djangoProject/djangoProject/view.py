from djangoProject import LFM
from django.http import HttpResponse


def fresh_recommend(request):
    LFM.run_LFM()
    return HttpResponse("ok")
