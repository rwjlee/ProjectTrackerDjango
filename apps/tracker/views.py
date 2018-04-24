from django.shortcuts import render, redirect
from apps.tracker.models import Project, Task
from apps.user_info.models import User
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect('user_info:login')

    context = {
        'projects': Project.objects.filter(user_id = request.session['user_id'])
    }

    return render(request, 'tracker/index.html', context)

def create_project(request):
    if 'user_id' not in request.session:
        return redirect('user_id:login')

    html_name = request.POST['html_name']
    html_user_id = request.session['user_id']

    project = Project.objects.create(name = html_name, user_id = html_user_id)

    return redirect('tracker:index')

def project_index(request, project_id):
    if 'user_id' not in request.session:
        return redirect('user_info:login')
    
    db_tasks = Task.objects.filter(project_id = project_id)
    print(len(db_tasks))
    context = {
        'project': Project.objects.get(id = project_id),
        'tasks': db_tasks
    }

    return render(request, 'tracker/project_index.html', context)

def add_task(request):
    if 'user_id' not in request.session:
        return redirect('user_id:login')

    html_name = request.POST['html_task_name']
    html_project_id = request.POST['html_project_id']

    print('+++++++')
    print(html_name)
    print(html_project_id)

    task = Task.objects.create(name = html_name, project_id = html_project_id)

    return redirect('tracker:project_index', project_id=html_project_id)