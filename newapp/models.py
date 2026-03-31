from django.db import models

# Create your models here.
class schl(models.Model):
    schl_id=models.IntegerField(unique=True)
    schl_name=models.CharField(max_length=30)
