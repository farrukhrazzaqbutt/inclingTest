from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('api/tasks_list', views.tasks_list,name="api/tasks_list"),
    path('api/tiles_list', views.tiles_list,name="api/tiles_list"),
    path('api/task_detail/<int:pk>', views.task_detail,name="api/task_detail"),
    path('api/tile_detail/<int:pk>', views.tile_detail,name="api/tile_detail"),

    ]