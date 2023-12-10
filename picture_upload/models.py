from django.db import models

class PictureUpload(models.Model):
    image = models.ImageField(verbose_name='image', upload_to='img/')

    class Meta:
        verbose_name_plural = 'picture_upload'