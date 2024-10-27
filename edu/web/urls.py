from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="main_page"),
    path("meetings/", views.meetings, name="meetings"),
    path('meeting-details/<int:id>/', views.meeting_details, name='meeting-details'),
]
