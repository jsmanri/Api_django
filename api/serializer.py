from rest_framework import serializers
from .models import programmer , student


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model= programmer
        #fields = ('full_name','nickname','age')
        fields = '__all__'
        
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model= student
        #fields = ('full_name','nickname','age')
        fields = '__all__'