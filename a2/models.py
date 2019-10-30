from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=6)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', default=None)

    def __str__(self):
        return self.title
