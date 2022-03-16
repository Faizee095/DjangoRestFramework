from functools import partial
import imp
from pickle import NONE
from django.shortcuts import render
from django.urls import is_valid_path
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated

def StudentDetail(request,pk):
    stu=Student.objects.get(id = pk)
    ser1=StudentSerializer(stu)
    # jsonData=JSONRenderer().render(ser1.data)
    # return HttpResponse(jsonData,content_type='application/json')
    #above 2 line can be substituted with this
    return JsonResponse(ser1.data)

#QuerySet
def Studentlist(request):
    stu=Student.objects.all()
    ser1=StudentSerializer(stu,many=True)
    jsonData=JSONRenderer().render(ser1.data)

    return HttpResponse(jsonData,content_type='application/json')

@csrf_exempt
def StudentCreate(request):
    print(request)
    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        ser=StudentSerializer(data=parsed_data)
        if ser.is_valid():
            ser.save()
            resp={'msg': 'User Created'}
            # jsonData=JSONRenderer().render(resp)
            # return HttpResponse(jsonData,content_type='application/json')
            return JsonResponse(resp)

    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        ser=StudentSerializer(stu,data=parsed_data,partial=True)
        #for compelte update
        #ser=StudentSerializer(stu,data=parsed_data)
        if ser.is_valid():
            ser.save()
            resp={'msg': 'User Updated'}
            return JsonResponse(resp)

    if request.method =='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        resp={'msg': 'User Deleted'}
        return JsonResponse(resp)


        return JsonResponse(ser.errors)


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queeyset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_Class=[JWTAuthentication]
#     permission_class=[IsAuthenticated]

