from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('quality/', include('quality_control.urls'))
]
