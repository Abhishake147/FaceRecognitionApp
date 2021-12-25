from django.db import models
from django.contrib.auth.models import User

def rename_image(instance, filename):
    return 'C://Users//crazy//PycharmProjects//ImageformProject//media//img//' + instance.name + '.png'

class Image(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to=rename_image)
    def __str__(self):
        return self.name








