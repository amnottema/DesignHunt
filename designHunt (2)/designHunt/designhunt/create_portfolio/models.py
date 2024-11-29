from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/')
    figma = models.URLField()
    telegram = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

class PortfolioFile(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='portfolios/')

    def __str__(self):
        return self.file.name