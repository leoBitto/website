from django.urls import path, include
from . import views

app_name="website"
urlpatterns = [
    path('', views.base, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
]