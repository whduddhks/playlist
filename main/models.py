from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Myplaylist(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    writer = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField()
    body = models.TextField(null=False, blank=False)
    list_type = models.CharField(max_length=50, null=False, blank=False)
    list_genre = models.CharField(max_length=50, null=False, blank=False) 
    list_play = models.CharField(max_length=50, null=False, blank=False)
    list_image = models.ImageField(null=False, upload_to = 'playlist/')
    user=models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]