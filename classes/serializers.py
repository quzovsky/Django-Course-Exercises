from rest_framework import serializers
from.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=['name','capacity','department','area']
    def validate(self,data):
        if data.get('capacity',0)<5:
            raise serializers.ValidationError()
        if data.get('area',0)<0:
            raise serializers.ValidationError()
        return data