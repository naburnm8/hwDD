from django.urls import path
from quality_control import views

app_name = 'quality_control'



urlpatterns = [
    path('', views.index, name='main'),
    path('bugs/', views.bug_report_list, name='bugs'),
    path('features/', views.feature_report_list, name='features'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_details'),
    path('features/<int:features_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/new/', views.report_bug, name='bug_new'),
    path('features/new/', views.request_feature, name='feature_new')
]
