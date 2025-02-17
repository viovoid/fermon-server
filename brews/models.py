from django.db import models
from django.utils import timezone
from enum import Enum

class Category(Enum):
  MANA = 0
  ALCOHOL = 1
  FUNGUS = 2
  VEGETABLE = 3

class Brew(models.Model):
  ident = models.CharField(max_length=32)
  category = models.CharField(
    max_length=16,
    choices=[(cat.name, cat.name) for cat in Category],
    default=Category.VEGETABLE.name
  )
  init_date = models.DateTimeField(default=timezone.now)
  ingredients = models.TextField()

  def __str__(self):
    return self.ident

class Update(models.Model):
  brew = models.ForeignKey(Brew, related_name='updates', on_delete=models.CASCADE)
  post_date = models.DateTimeField(default=timezone.now)
  body = models.TextField()

  def __str__(self):
    return self.id
