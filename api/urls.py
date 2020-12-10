from django.urls import path
from api import views as api_views

urlpatterns=[
    path('',api_views.apiOverview, name="api-overview"),
    path('task-list/',api_views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', api_views.taskDetail, name="task-detail"),
    path('task-create/',api_views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', api_views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', api_views.taskDelete, name="task-delete"),
]