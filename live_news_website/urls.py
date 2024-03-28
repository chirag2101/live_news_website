from django.contrib import admin
from django.urls import path,include
from news_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news_api/',include('news_api.url'),),
    path('',views.home,name='home'),
]


