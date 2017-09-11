from rest_framework import viewsets
from apartment_project.modules.serializers import UserSerializer
from apartment_project.modules.models import Cleaning, User


class getUsers(viewsets.ModelViewSet):
    queryset = User.objects.all()
    print("+++++" , len(queryset))
    serializer_class = UserSerializer