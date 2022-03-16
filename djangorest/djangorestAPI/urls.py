from django.contrib import admin
from django.urls import path
from djangorestAPI import views

urlpatterns = [
    path('stuinfo/<int:pk>/',views.StudentDetail,name='info' ),
    path('stuinfo/',views.Studentlist,name='list' ),
    path('stucreate/',views.StudentCreate,name='Create' ),
    path('stuupdate/',views.StudentCreate,name='Update' ),
]
