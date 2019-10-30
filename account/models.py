from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.conf import settings
User = get_user_model()


class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics', default=None)
    price = models.IntegerField(max_length=10, blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.now())
    quantity = models.IntegerField(max_length=2, default=1)
    total_price = models.IntegerField(max_length=10, blank=True, null=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

class Coupon(models.Model):
    codes = models.CharField(max_length=10, blank=True, null=True)
    discount = models.IntegerField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.codes

