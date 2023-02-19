from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField()
    description = models.CharField(max_length=256)
    blog_text = models.TextField()

    def __str__(self):
        return self.title
