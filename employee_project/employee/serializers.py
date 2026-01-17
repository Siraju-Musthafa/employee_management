from rest_framework import serializers
from .models import employeetable


class employeeserializers(serializers.ModelSerializer):
 
    class Meta:
        model=employeetable
        fields='__all__'
    def validate_email(self,value):
     if employeetable.objects.filter(email=value).exists():
          if self.instance and self.instance.email ==value:
               return value
          raise serializers.ValidationError('Email must be unique')
     return value
     
