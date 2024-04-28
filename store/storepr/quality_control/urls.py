from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='main'),
    path('bugs/', views.bugs, name='bugs'),
    path('features/', views.features, name='features'),
    path('bugs/<int:bug_id>', views.bug_detail),
    path('features/<int:features_id>', views.features_id_detail),
]