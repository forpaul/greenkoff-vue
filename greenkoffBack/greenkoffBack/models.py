from django.db import models


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=1000)
    price = models.IntegerField(blank=False, null=False)
    position = models.IntegerField(blank=False, null=False)
    image1 = models.FileField(upload_to="productImages/", blank=True, null=True)
    image2 = models.FileField(upload_to="productImages/", blank=True, null=True)
    image3 = models.FileField(upload_to="productImages/", blank=True, null=True)
    image4 = models.FileField(upload_to="productImages/", blank=True, null=True)


class Service(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=1000)
    price = models.IntegerField(blank=False, null=False)

