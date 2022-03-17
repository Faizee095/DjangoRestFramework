from django.contrib import admin
from django.urls import path
# from .views import StudentModelViewSet
from djangorestAPI import views

urlpatterns = [
    # path('stuinfo/<int:pk>/',views.StudentDetail,name='info' ),
    # path('stuinfo/',views.Studentlist,name='list' ),
    # path('stucreate/',views.StudentCreate,name='Create' ),
    # path('stuupdate/',views.StudentCreate,name='Update' ),
    # path('stuview/',StudentModelViewSet.as_view({'get': 'list'}), name='view' ),
    # path('stuapi/',views.StudentApi.as_view(),name='api' ),
    path('stuapi/',views.StudentApi,name='api' ),
    path('stuapi/<int:pk>/',views.StudentApi,name='api' ),
]
