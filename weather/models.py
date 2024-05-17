from django.db import models

# Create your models here.
class UserLocale(models.Model):
    country = models.CharField(max_length=100)
    federation = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        if (self.federation == None):
            return  self.city + ',' + self.country
        else:
            return  self.city + ',' + self.federation + ',' + self.country