from django.contrib import admin
from django.urls import path
from live_news_website import views
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.home,name='home'),

]
