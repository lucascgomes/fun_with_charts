from django.db import models

# Create your models here.

class Chart(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class TimeStamp(models.Model):
    chart = models.ForeignKey(Chart)
    time = models.FloatField(unique=True)
    value = models.FloatField()

    def __unicode__(self):
        return str(self.time)
