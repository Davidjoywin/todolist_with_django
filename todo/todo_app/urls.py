from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.home, name="home"),
    path("signup", views.register_user, name="signup"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("<int:pk>/notes", views.add_note, name="note"),
    path("<int:pk>/notes/<int:fk>/deletes", views.delete_note, name="delete_note"),
    path("delete/<int:pk>", views.delete_task, name="delete"),
]