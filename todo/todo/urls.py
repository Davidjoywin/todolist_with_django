from http.client import HTTPResponse
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("favicon.ico", lambda request : HttpResponse("successful")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("todo/", include("todo_app.urls")),
]
