from django.db import models
from django.utils import timezone

class Brew(models.Model):
  ident = models.TextField()
  init_date = models.DateTimeField(
    default = timezone.now)
  ingredients = models.TextField()

  def __str__(self):
    return self.ident
