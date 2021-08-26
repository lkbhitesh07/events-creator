from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    location = models.TextField()
    image = models.ImageField(upload_to = 'event_images')
    is_liked = models.BooleanField(default = False)

    def __str__(self):
        return self.event_name