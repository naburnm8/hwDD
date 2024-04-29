from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from quality_control.models import BugReport, FeatureRequest


def index(request):
    bugs_url = reverse('quality_control:bugs')
    features_url = reverse('quality_control:features')
    html = (f"<h1>Страница приложения quality_control</h1><a href='{bugs_url}'>Перейти страницу отчётов о багах<br></a>"
            f"<a href='{features_url}'>Перейти на страницу запросов на улучшение</a>")
    return HttpResponse(html)


class IndexVew(View):
    def index(self, request, *args, **kwargs):
        bugs_url = reverse('quality_control:bugs')
        features_url = reverse('quality_control:features')
        html = (
            f"<h1>Страница приложения quality_control</h1><a href='{bugs_url}'>Перейти страницу отчётов о багах<br></a>"
            f"<a href='{features_url}'>Перейти на страницу запросов на улучшение</a>")
        return HttpResponse(html)


def bug_report_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список bugs</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title} статус: {bug.status}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p><p>Статус: {bug.status}</p><p>Уровень приоритета: {bug.priority}</p><p>Проект: {bug.project}</p><p>Связанная задача: {bug.task}</p>'
        return HttpResponse(response_html)


def feature_report_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список features</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title} статус: {feature.status}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p><p>Статус: {feature.status}</p><p>Уровень приоритета: {feature.priority}</p><p>Проект: {feature.project}</p><p>Связанная задача: {feature.task}</p>'
        return HttpResponse(response_html)
