from django.db import models

class PictureUpload(models.Model):
    image = models.ImageField(upload_to='img/')