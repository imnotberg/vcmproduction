from .models import *
from rest_framework import serializers

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
'''
class AwardsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Award
		fields = '__all__'
