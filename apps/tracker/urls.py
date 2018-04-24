from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project', views.create_project, name = 'create_project'),
    path('project_index/<int:project_id>', views.project_index, name = 'project_index'),
    path('add_task', views.add_task, name = 'add_task')
]