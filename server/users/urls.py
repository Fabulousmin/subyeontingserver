# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('facebook/',views.FacebookLogin.as_view()),
]
