from django.db import models

# Create your models here.


from django.db import models
from django.conf import settings
from django.utils import timezone

class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=300)
  quantity=models.IntegerField()
  price=models.FloatField()
  discount=models.IntegerField()
  offer=models.BooleanField()
  image=models.CharField(max_length=300)

class Ticket(models.Model):
  date = models.DateTimeField(default=timezone.now)
  file_path=models.CharField(max_length=300)








