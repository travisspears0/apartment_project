from rest_framework import serializers
from apartment_project.modules.models import Cleaning, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'avatar', 'email', 'admin')
