from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    ProductId=models.IntegerField()
    ProductName=models.CharField(max_length=15)
    CategoryId=models.IntegerField()
    CategoryName=models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
