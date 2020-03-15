from django.db import models


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=1000)
    price = models.IntegerField(blank=False, null=False)
    position = models.IntegerField(blank=False, null=False)


class Service(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=1000)
    price = models.IntegerField(blank=False, null=False)

