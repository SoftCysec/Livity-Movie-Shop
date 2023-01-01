from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    poster_image = models.URLField()
    plot_summary = models.TextField()

    def __str__(self):
        return self.title