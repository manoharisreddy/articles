from django.urls import path
from . import views


urlpatterns=[

path('',views.Home,name='Home'),

path('news/',views.News,name='News'),

path('events/',views.Events,name='Events'),

path('about/',views.About,name='About'),

path('read/<int:id>/',views.read,name='read'),

]