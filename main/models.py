from django.db import models


class Resent(models.Model):
    code = models.CharField(max_length=10)
    price = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return self.code
# Create your models here.
