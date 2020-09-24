from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('shop', views.shoppage, name='shop'),
    path('video', views.videopage, name='video'),
    path('gaming-setup', views.gamingsetuppage, name='gamingsetuppage'),
    path('custom-pc-build', views.customPcBuild, name='custom-pc-build'),
    path('racing-simulator', views.racingSimulator, name='racing-simulator'),
    path('accessories', views.accessories, name='accessories'),



]