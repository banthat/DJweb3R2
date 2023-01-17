from django.urls import path
from ProfileApp import views

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('hello', views.helloworld, name='hello',),
    path('firstpage', views.firstPage, name='firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('hnypage', views.hnypage, name='hnypage'),
]