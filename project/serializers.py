from .models import *
from rest_framework import serializers

class AwardsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Awards
		fields = ['organization']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_staff']