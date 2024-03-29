from rest_framework import serializers

from .models import Hobby, Student

#Validators
# def start_with_f(value):
#     if value[0].lower() !='f':
#         raise serializers.ValidationError('Name must startwith f')
#     return value



#Normal Serializer
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=50)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)



#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)


#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance

    #Feild Level validation
    # def validate_roll(self,value):
    #     if value >100:
    #         raise serializers.ValidationError('Seat Full')
        
    #     return value

    #Object Level Validators
    # def validate(self,value):
    #     nm=value.get('name')
    #     ct=value.get('city')
    #     if nm=='fasif' and ct !='muz':
    #         raise serializers.ValidationError('City must be muz')
    #     return value


#Modern Serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields ='__all__'
        # read_only_fields =['name']    #validator
        #extra_kwargs={'name':{'read_only':True}}     #we can give multiple validators using this


    # def validate_roll(self, value):
    #     if value >100 :
    #         raise serializers.ValidationError('Seat Full')
    #     return value
        
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model =Hobby
        fields= '__all__'