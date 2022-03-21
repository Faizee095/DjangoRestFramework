from multiprocessing.spawn import import_main_path
import django
from django.db import models

    
class Hobby(models.Model):
    #student= models.OneToOneField(Student, on_delete=models.CASCADE,primary_key=True)
    time=models.IntegerField()
    hobby_name=models.CharField(max_length=50)

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    hobies = models.ManyToManyField(Hobby, related_name='hobbys')


#Genarate token using signal:
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
