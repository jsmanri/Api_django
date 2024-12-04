from django.db import models

# Create your models here.
# aqui se crean los modelos (tablas o colecciones)
class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None )
    is_active = models.BooleanField(default=True)


class student(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)