from django.db import models
from datetime import date

class turiste(models.Model):
    Destination = models.CharField(max_length=100)
    Distence = models.IntegerField(default=00)
    visit_image = models.ImageField(max_length=None, upload_to="picture", default="default_image.png")
    location = models.FileField(upload_to="files/", default="path/to/default/file.txt")


class visitor(models.Model):
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    timeing = models.TimeField(default="00:00:00")

    
# Create your models here.
