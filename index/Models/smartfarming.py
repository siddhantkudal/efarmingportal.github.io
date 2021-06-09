from django.db import models

class smartfar(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploaded/images')
    def __str__(self):
        return self.name