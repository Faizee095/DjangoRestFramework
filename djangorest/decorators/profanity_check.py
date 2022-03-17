# from djangorestAPI.views import Student
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse,JsonResponse
# import io
# from rest_framework.parsers import JSONParser
# from profanity_check import predict, predict_prob


# def profanity(function):
#     def decorator(*args, **kwargs):
#         #print (args[0])
#         json_data=args[0].body
#         stream=io.BytesIO(json_data)
#         parsed_data=JSONParser().parse(stream)
#         print(parsed_data)
#         for k,v in parsed_data.items():
#             if k =='profanity':
#                 for k,v in parsed_data.items():
#                     if predict([v]) is [1]:
#                          return HttpResponse('Data is not correct.  Please avoid any profanities')
#         return function(*args, **kwargs)

#     return decorator










