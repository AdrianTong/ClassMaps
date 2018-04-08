from django.urls import path, re_path
from . import views
from .views import search

app_name = 'classes'
urlpatterns = [
    path('', views.index, name="index"),
    path('results/', search, name="search"),
    re_path(r'details/(?P<id>\d+)/', views.details, name="details"),
];