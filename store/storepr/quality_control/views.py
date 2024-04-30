from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest

from .forms import BugReportForm, FeatureRequestForm


def index(request):
    return render(request, 'quality_control/index.html')


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
    return render(request, 'quality_control/bug_report.html', {'bug_list': bugs})



class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_report_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_report.html', {'feature_list': features})

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def report_bug(request):
    if request.method == 'POST':
        bug = BugReportForm(request.POST)
        if bug.is_valid():

            bug.save()
            return redirect('quality_control:bugs')
    else:
        bug = BugReportForm()
    return render(request, 'quality_control/report_bug.html', {'bug': bug})

def request_feature(request):
    if request.method == 'POST':
        feature = FeatureRequestForm(request.POST)
        if feature.is_valid():
            feature.save()
            return redirect('quality_control:features')
    else:
        feature = BugReportForm()
    return render(request, 'quality_control/new_feature.html', {'feature': feature})

