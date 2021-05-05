from django.urls import path

from .views import apiOverView, taskList, taskDetail, taskCreate, taskUpdate, taskDelete



urlpatterns = [
    path('', apiOverView, name='apiOverView'),
    path('task-list/', taskList, name='taskList'),
    path('task-detail/<str:pk>/', taskDetail, name='taskDetail'),
    path('task-create/', taskCreate, name='taskCreate'),
    path('task-update/<str:pk>/', taskUpdate, name='taskUpdate'),
    path('task-delete/<str:pk>/', taskDelete, name='taskDelete'),   
]
