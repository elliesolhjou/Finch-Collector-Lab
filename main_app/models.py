from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    threats=models.TextField(max_length=255)
    habitat=models.TextField(max_length=255, null=True)

    def __str__(self):
        return f'{(self.name)} has {self.breed} breed'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
