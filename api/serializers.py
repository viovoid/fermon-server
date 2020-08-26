from django.contrib.auth.models import User
from brews.models import Brew, Update
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'is_staff']

class UpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Update
    fields = ['id', 'brew', 'post_date', 'body']

class BrewSerializer(serializers.ModelSerializer):
  updates = UpdateSerializer(many=True, read_only=True)
  class Meta:
    model = Brew
    fields = ['id', 'ident', 'category', 'init_date', 'ingredients', 'updates']
