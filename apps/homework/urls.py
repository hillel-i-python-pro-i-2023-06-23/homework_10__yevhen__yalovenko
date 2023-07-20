from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
    path("story/<name>/", views.generate_users, name="generate_users"),
    path("story/<name>/<int:amount>/", views.generate_users, name="generate_users"),
]
