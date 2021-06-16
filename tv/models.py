from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Tv(models.Model):
    brand = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('tv_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.brand
