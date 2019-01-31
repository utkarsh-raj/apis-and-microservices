from django.urls import path
from . import views

urlpatterns = [
    path("exercise/new-user", views.create_user, name="create_user"),
    path("exercise/add", views.create_exercise, name="create_exercise"),
    path("exercise/log", views.get_description, name="get_description"),
    path("exercise/users", views.get_users, name="get_users"),
]