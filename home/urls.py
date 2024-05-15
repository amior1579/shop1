from django.urls import path, include
from . import views
from home import views

app_name = 'home-web'

urlpatterns = [
    path("", views.index, name="home"),
]
