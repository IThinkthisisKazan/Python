from django.db import models

# Create your models here.
class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000, blank=False)
    date = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title