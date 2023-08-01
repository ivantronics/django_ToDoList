from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.view_list, name="index"),
    path("", views.home, name="home"),
    path("new_list/", views.new_list, name="new_list"),
    path("latest_list/", views.latestlist, name="latestlist"),
    path("confirmation_<int:pk>/", views.confirmation, name="confirmation"),
]
