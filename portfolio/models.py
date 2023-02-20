from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=124)
    description = models.CharField(max_length=248)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=124)
    description = models.CharField(max_length=248)
    image = models.ImageField(upload_to='certificate/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
