from re import A
from django.shortcuts import render
from django.urls import is_valid_path
from .models import Student,Hobby
from .serializer import StudentSerializer,HobbySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from decorators.profanity_check import profanity
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated


#function based View
# def StudentDetail(request,pk):
#     stu=Student.objects.get(id = pk)
#     ser1=StudentSerializer(stu)
#     # jsonData=JSONRenderer().render(ser1.data)
#     # return HttpResponse(jsonData,content_type='application/json')
#     #above 2 line can be substituted with this
#     return JsonResponse(ser1.data)

# #QuerySet
# def Studentlist(request):
#     stu=Student.objects.all()
#     ser1=StudentSerializer(stu,many=True)
#     jsonData=JSONRenderer().render(ser1.data)
#     return HttpResponse(jsonData,content_type='application/json')


# @csrf_exempt
# @profanity
# def StudentCreate(request):
#     print(request)
#     if request.method =='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         ser=StudentSerializer(data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Created'}
#             # jsonData=JSONRenderer().render(resp)
#             # return HttpResponse(jsonData,content_type='application/json')
#             return JsonResponse(resp)

#     if request.method =='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         id=parsed_data.get('id')
#         stu=Student.objects.get(id=id)
#         ser=StudentSerializer(stu,data=parsed_data,partial=True)
#         #for compelte update
#         #ser=StudentSerializer(stu,data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Updated'}
#             return JsonResponse(resp)
    

#     if request.method =='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         id=parsed_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg': 'User Deleted'}
#         return JsonResponse(resp)


#     return JsonResponse(ser.errors)


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queeyset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_Class=[JWTAuthentication]
#     permission_class=[IsAuthenticated]


#Class based view::-->>

# from django.utils.decorators import method_decorator
# from django.views import View

# @method_decorator(csrf_exempt,name='dispatch')
# class StudentApi(View):

#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         id=parsed_data.get('id')
#         if id >0:
#             stu=Student.objects.get(id = id)
#             ser1=StudentSerializer(stu)
#             return JsonResponse(ser1.data)
#         stu=Student.objects.all()
#         ser1=StudentSerializer(stu,many=True)
#         return JsonResponse(ser1.data,safe=False)

#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         ser=StudentSerializer(data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Created'}
#             # jsonData=JSONRenderer().render(resp)
#             # return HttpResponse(jsonData,content_type='application/json')
#             return JsonResponse(resp)

#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         id=parsed_data.get('id')
#         stu=Student.objects.get(id=id)
#         ser=StudentSerializer(stu,data=parsed_data,partial=True)
#         #for compelte update
#         #ser=StudentSerializer(stu,data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Updated'}
#             return JsonResponse(resp)

#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         id=parsed_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg': 'User Deleted'}
#         return JsonResponse(resp)


#FUnction based Api View
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def StudentApi(request,pk=NONE):
#     if request.method == 'GET':
#         # id =request.data.get('id')
#         id=pk
#         if id is not NONE:
#             stu=Student.objects.get(id=id)
#             ser=StudentSerializer(stu)
#             return Response(ser.data)
#         stu=Student.objects.all()
#         ser=StudentSerializer(stu,many=True)
#         return Response(ser.data)

#     if request.method =='POST':
#         ser=StudentSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Created'}
#             # jsonData=JSONRenderer().render(resp)
#             # return HttpResponse(jsonData,content_type='application/json')
#             return Response(resp,status=status.HTTP_201_CREATED)

#     if request.method =='PUT':
#         id=request.data.get('id')
#         stu=Student.objects.get(id=id)
#         ser=StudentSerializer(stu,data=request.data,partial=True)
#         #for compelte update
#         #ser=StudentSerializer(stu,data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Updated'}
#             return Response(resp)

#     if request.method =='DELETE':
#         # id=request.data.get('id')
#         id =pk
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg': 'User Deleted'}
#         return Response(resp)

#     return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


# Class based API View

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# class StudentApi(APIView):
#     def get(self,request,pk=NONE,format=NONE):
#         id=pk
#         if id is not NONE:
#             stu=Student.objects.get(id=id)
#             ser=StudentSerializer(stu)
#             return Response(ser.data)
#         stu=Student.objects.all()
#         ser=StudentSerializer(stu,many=True)
#         return Response(ser.data)


#     def post(self,request,format=None):
#         ser=StudentSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Created'}
#             # jsonData=JSONRenderer().render(resp)
#             # return HttpResponse(jsonData,content_type='application/json')
#             return Response(resp,status=status.HTTP_201_CREATED)
#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


    
#     def put(self,request,pk=None,format=None):
#         id=pk
#         stu=Student.objects.get(id=id)
#         ser=StudentSerializer(stu,data=request.data,partial=True)
#         #for compelte update
#         #ser=StudentSerializer(stu,data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Updated'}
#             return Response(resp)
#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk=None,format=None):
#         id =pk
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg': 'User Deleted'}
#         return Response(resp)


#Generic API view and Model Mixin
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# from djangorestAPI import serializer


# class StudentList(ListModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

#List and create dont require pk so we can combine them
# class StudentListCreate(ListModelMixin,GenericAPIView,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class StudentRetreive(GenericAPIView,RetrieveModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)


# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


# class StudentDelete(GenericAPIView,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

#Retreive ,Update and delete requires pk so they can be grouped together
# class StudentRetreive_Update_Delete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



#Concrete View Class

# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

# class StudentList(ListAPIView,CreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentListRUD(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#There is some thing we can use also ListCreateAPIView and RetrieveUpdateDestroyAPIView
# class StudentList(ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentListRUD(RetrieveUpdateDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


#ViewSet Class

# from rest_framework import viewsets
# from rest_framework.response import Response

# class StudentViewSet(viewsets.ViewSet):
#     def List(self,request):
#         stu=Student.objects.all()
#         ser1=StudentSerializer(stu,many=True)
#         return Response(ser1.data,safe=False)

#     def retrieve(self,request,pk=None):
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             ser=StudentSerializer(stu)
#             return Response(ser.data)
#         stu=Student.objects.all()
#         ser=StudentSerializer(stu,many=True)
#         return Response(ser.data)

#     def create(self,request):
#         ser=StudentSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Created'}
#             return Response(resp)
#         return Response(ser.error)

#     def delete(self,request,pk=None):
#         id =pk
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg': 'User Deleted'}
#         return Response(resp)


#     def update(self,request,pk=None):
#         id=pk
#         stu=Student.objects.get(id=id)
#         ser=StudentSerializer(stu,data=request.data,partial=True)
#         #for compelte update
#         #ser=StudentSerializer(stu,data=parsed_data)
#         if ser.is_valid():
#             ser.save()
#             resp={'msg': 'User Updated'}
#             return Response(resp)
#         return Response(ser.errors)

#Model View Set and Ready Only Model View Set
# from rest_framework import viewsets


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


#Basic Authentication
# from rest_framework import viewsets
# from rest_framework.authentication  import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # permissions_classes=[IsAuthenticated]


#Session Authentication
# from rest_framework import viewsets
# from rest_framework.authentication  import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[SessionAuthentication]
#     # permissions_classes=[IsAuthenticatedOrReadOnly]
#     permissions_classes=[DjangoModelPermissions]


#Token Based Autentication
# from rest_framework import viewsets
# from rest_framework.authentication  import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[TokenAuthentication]
#     permissions_classes=[IsAuthenticated]
    # permissions_classes=[DjangoModelPermissions]


#JWT Authentication
from rest_framework import viewsets
from  rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[JWTAuthentication]
    permissions_classes=[IsAuthenticated]