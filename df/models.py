from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.auth.models import User


# Create your models here.
class Dataframe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    df_name = models.CharField(max_length=255)
    data = PickledObjectField()


class DataframeFilled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    df_name = models.CharField(max_length=255)
    data = PickledObjectField()
