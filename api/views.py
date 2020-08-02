from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from brews.models import Brew, Update
from .serializers import UserSerializer, BrewSerializer, UpdateSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BrewViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows brews to be viewed or edited.
  """
  queryset = Brew.objects.all()
  serializer_class = BrewSerializer

class UpdateViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows updates to be viewed or edited.
  """
  queryset = Update.objects.all()
  serializer_class = UpdateSerializer
