from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', homepageView.as_view(), name="home"),
    path('about/',aboutpageView.as_view(), name="about"),
] 