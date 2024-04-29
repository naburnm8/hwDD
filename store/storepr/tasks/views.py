from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Project, Task


def index(request):
    projects_list_url = reverse('tasks:projects_list')
    quality_page_url = reverse('quality_control:main')
    html = (f"<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>Список проектов<br></a>"
            f"<a href='{quality_page_url}'>Перейти на страницу приложения quality_control<br></a>")
    return HttpResponse(html)


def projects_list(request):
    projects = Project.objects.all()
    projects_html = '<h1>Список проектов</h1><ul>'
    for project in projects:
        projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
    projects_html += '</ul>'
    return HttpResponse(projects_html)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()
    response_html = f'<h1>{project.name}</h1><p>{project.desc}</p>'
    response_html += '<h2>Задачи</h2><ul>'
    for task in tasks:
        response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
    response_html += '</ul>'
    return HttpResponse(response_html)


def task_detail(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id, project=project)
    response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
    return HttpResponse(response_html)