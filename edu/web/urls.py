from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="main_page"),
]