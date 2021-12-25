from django.urls import path
from home import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('index', views.index, name='index'),
    path('screenshots', views.screenshots, name='screenshots'),
    path('authentication', views.authentication, name='authentication'),
]