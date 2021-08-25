from django.db import models

# Create your models here.
class event(models.Model):
    event_title=models.CharField(max_length=50)
    event_desc=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    event_date=models.DateField()
