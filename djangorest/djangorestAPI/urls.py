from django.contrib import admin
from django.urls import path,include
# from .views import StudentModelViewSet
from djangorestAPI import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#Setting up router for viewset
router=DefaultRouter()
router.register('stuapi', views.StudentModelViewset ,basename='student')


urlpatterns = [
    # path('stuinfo/<int:pk>/',views.StudentDetail,name='info' ),
    # path('stuinfo/',views.Studentlist,name='list' ),
    # path('stucreate/',views.StudentCreate,name='Create' ),
    # path('stuupdate/',views.StudentCreate,name='Update' ),
    # path('stuview/',StudentModelViewSet.as_view({'get': 'list'}), name='view' ),
    # path('stuapi/',views.StudentApi.as_view(),name='api' ),
    #Function based Api view
    # path('stuapi/',views.StudentApi,name='api' ),
    # path('stuapi/<int:pk>/',views.StudentApi,name='api' ),
    # Class Based Api View
    # path('stuapi/',views.StudentApi.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentApi.as_view(),name='api' ),
    #Generic API view and Model Mixin
    # path('stuapi/',views.StudentList.as_view(),name='api' ),
    # path('stuapi/',views.StudentCreate.as_view(),name='api' ),
    # path('stuapi/',views.StudentListCreate.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentRetreive.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentUpdate.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentDelete.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentRetreive_Update_Delete.as_view(),name='api' ),
    #Concrete View Class
    # path('stuapi/',views.StudentList.as_view(),name='api' ),
    # path('stuapi/<int:pk>/',views.StudentListRUD.as_view(),name='api' ),
    #ViewSet Class
    path('',include(router.urls)),
    #Session Authentication
    # path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    #Token Authentication
    # path('gettoken/',obtain_auth_token),
    #JWT 
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]
