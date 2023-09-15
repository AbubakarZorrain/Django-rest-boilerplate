from .models import *
from rest_framework import serializers

class myModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModel
        fields = '__all__'