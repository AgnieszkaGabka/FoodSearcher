from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'foodies'

    def __str__(self):
        return self.name
