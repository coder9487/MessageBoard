from django.db import models

# Create your models here.


class Post(models.Model):
    timestemp   = models.CharField(max_length=20)
    message     = models.TextField()
    username    = models.CharField(max_length=20)

    
