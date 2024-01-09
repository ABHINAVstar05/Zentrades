from django.db import models

# Create your models here.


class Products(models.Model):
    subcategory = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    popularity = models.IntegerField()

    def __str__(self) -> str:
        return self.title
