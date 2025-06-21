from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class ImageColor(models.Model):
    image = models.ImageField(upload_to='uploads/')
    thumbnail = models.ImageField(upload_to='uploads/thumbs/', null=True, blank=True) # Helps in loading entire image list faster
    hex_color = models.CharField(max_length=7, blank=True, null=True)