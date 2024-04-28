from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bugs_url = reverse('quality_control:bugs')
    features_url = reverse('quality_control:features')
    html = (f"<h1>Страница приложения quality_control</h1><a href='{bugs_url}'>Перейти страницу отчётов о багах<br></a>"
            f"<a href='{features_url}'>Перейти на страницу запросов на улучшение</a>")
    return HttpResponse(html)


def bugs(request):
    return HttpResponse("Cписок отчетов об ошибках")


def features(request):
    return HttpResponse("Список запросов на улучшение")


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def features_id_detail(request, features_id):
    return HttpResponse(f"Детали улучшения {features_id}")


