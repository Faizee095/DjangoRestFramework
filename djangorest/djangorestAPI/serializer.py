from rest_framework import serializers

from .models import Student

#Validators
def start_with_r(value):
    if value[0].lower() !='r':
        raise serializers.ValidationError('Name must startwith r')
    return value

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)



    def create(self,validate_data):
        return Student.objects.create(**validate_data)


    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

    #Feild Level validation
    def validate_roll(self,value):
        if value >100:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object Level Validators
    def validate(self,value):
        nm=value.get('name')
        ct=value.get('city')
        if nm=='rasif' and ct !='muz':
            raise serializers.ValidationError('City must be muz')
        raise value
