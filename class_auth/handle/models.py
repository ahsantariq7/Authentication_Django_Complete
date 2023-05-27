from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class my_store(models.Model):
    my_name=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='my_name',unique=True,null=True,default=None)
