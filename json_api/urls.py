from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("add_data", views.add_data , name="add_data"),
    path("delete", views.delete_data , name="delete"),
    path("show_data" , views.show_data , name="showdata")
]