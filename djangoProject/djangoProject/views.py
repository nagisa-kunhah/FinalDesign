from django.http import HttpResponse, JsonResponse


def work(request):
    h = '<h1>hello</h1>'
    tmp = HttpResponse(h)
    print(tmp)
    return tmp


def json(request):
    print(request.method)
    ret = JsonResponse({"a": 1, "b": 2})
    return ret


def recommend(request, user_id: int):
    h = '<h1>{}<h1>'.format(user_id)
    return HttpResponse(h)
