from django.urls import path
from . import views 

urlpatterns=[
    path('',views.stream,name='stream'),
    path('course/',views.course,name='course'),
    path('course/year/',views.year,name='year')


]