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