from django.db import models

# Create your models models here.

class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/')
    caption=models.TextField()
    