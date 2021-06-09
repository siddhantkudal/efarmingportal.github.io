from django.db import models

# Create your models here.
class mys(models.Model):
    Name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.Name
