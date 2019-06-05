from django.contrib import admin
from django.urls import path
from .views import Home_View,Feed_View

urlpatterns = [
    path('home/', Home_View.as_view()),
    path('feeds/', Feed_View,name="feed"),
]
