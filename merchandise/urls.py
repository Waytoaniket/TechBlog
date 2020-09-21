from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('shop', views.shoppage, name='shop'),
    path('video', views.videopage, name='video'),
    path('gaming-setup', views.gamingsetuppage, name='gamingsetuppage'),
]